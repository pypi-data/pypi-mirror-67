# -*- coding: utf-8 -*-

###
# Nathaniel Watson
# nathanielwatson@stanfordhealthcare.org
# 2019-05-16
###

import json
import logging
from multiprocessing import Process, Queue, Lock
import os
from pprint import pformat
import queue
import shutil
import signal
import sys
import tarfile
import traceback
import time

from google.cloud import storage, firestore

import psutil

import sruns_monitor as srm
import sruns_monitor.utils as utils
from sruns_monitor.sqlite_utils import Db
from sruns_monitor import exceptions as srm_exceptions


class Monitor:
    """
    Requires a configuration file in JSON format with settings regarding what folder to monitor
    and which GCP bucket to upload tarred runs to.
    """

    #: The presence of any file in this array indicates that the Run directory is ready for
    #: downstream processing (i.e. the Illumina NovaSeq has finished writing to the folder).
    #: The sential file can vary by sequencing platform. For NovaSeq, can use CopyComplete.txt.
    SENTINAL_FILES = set(["CopyComplete.txt"])

    def __init__(self, conf_file, verbose=True):
        """
        Args:
            conf_file: `str`. Path to JSON configuration file.
            verbose: `boolean`. True enables verbose logging. 
        """
        self.logger = logging.getLogger(__name__)
        #: Stores the value passed during instantiation to the parameter by the same name. 
        self.verbose = verbose
        #: Stores the validated JSON configuration file as a dictionary. Any top-level keys in the
        #: JSON file that were commented out (start with a '#') are not present here. 
        self.conf = utils.validate_conf(conf_file, schema_file=srm.CONF_SCHEMA)
        #: The name of the monitor. The name will appear in the subject line if email notification
        #: is configured, as well as in other places, i.e. log messages.
        self.monitor_name = self.conf[srm.C_MONITOR_NAME]
        #: The name of the Firestore collection to use. If not provided in configuration, will be
        #: None.
        self.firestore_collection = self.conf.get(srm.C_FIRESTORE_COLLECTION)
        if not self.firestore_collection:
            self.logger.warn("Firestore not enabled.")

        self.watchdirs = self.conf[srm.C_WATCHDIRS]
        # Make sure that all watch directories already exist:
        for path in self.watchdirs:
            if not os.path.exists(path):
                raise srm_exceptions.ConfigException("'watchdirs' is a required property and the referenced directory must exist.".format(path))
        #: The path to which processed runs will be moved to (last step of workflow). Run directories
        #: here are subjected to removal after a configurable amount of time; see the sweep_age_sec 
        #: config parameter. 
        self.completed_runs_dir = self.conf[srm.C_COMPLETED_RUNS_DIR]
        if not os.path.exists(self.completed_runs_dir):
            os.mkdir(self.completed_runs_dir)

        #: How old in minutes the sentinal file, i.e. CopyComplete.txt, should be before initiating
        #: any tasks, such as tarring the run directory. Illumina Support recommends 15 minutes, which
        #: is thus the default. 
        self.sentinal_file_age_minutes = self.conf.get(srm.C_SENTINAL_FILE_AGE_MINUTES, 15)
        #: When a run in the completed runs directory is older than this many seconds, remove it.
        #: If not specified in configuration file, defaults to 604800 (1 week).
        self.sweep_age_sec = self.conf.get(srm.C_SWEEP_AGE_SEC, 604800)
        #: The number of seconds to wait between run directory scans, with a default of 60.
        self.cycle_pause_sec = self.conf.get(srm.C_CYCLE_PAUSE_SEC, 60)
        #: The number of seconds that a child process running the workflow is allowed to run, after
        #: which the process will be killed. A value of 0 indicates that such a time limit will not
        #: be observed.
        self.process_runtime_limit_sec = self.conf.get(srm.C_TASK_RUNTIME_LIMIT_SEC, None)
        #: A `multiprocessing.Queue` instance that a child process will write to in the event that
        #: an Exception is to occur within that process prior to re-raising the Exception and exiting.
        #: The main process will check this queue in each scan iteration to report any child processes
        #: that have failed by means of logging and email notification.
        self.state = Queue() # Must pass in manually to multiprocessing.Process constructors.
        #: The GCP Storage bucket name in which tarred run directories will be stored.
        self.bucket_name = self.conf[srm.C_GCP_BUCKET_NAME]
        #: The directory in the bucket in which to store tarred run directories. If not provided,
        #: defaults to the root level directory.
        self.bucket_basedir = self.conf.get(srm.C_GCP_BUCKET_BASEDIR, "/")
        #signal.signal(signal.SIGTERM, self._cleanup)
        signal.signal(signal.SIGINT, self._cleanup)
        signal.signal(signal.SIGTERM, self._cleanup)
        #: The name of the local SQLite database.  Name defaults to sruns.db if not provided in
        #: the configuration.
        self.sqlite_dbname = self.conf.get(srm.C_SQLITE_DB, "sruns.db")
        #: A `sqlite3.Connection` instance.
        self.sqlite_conn = self.get_sqlite_conn()


    def get_firestore_conn(self):
        if self.firestore_collection:
            return firestore.Client().collection(self.firestore_collection)
        return False

    def get_sqlite_conn(self):
        """
        Creates a connection to the local SQLite database.

        Returns:
            `sqlite3.Connection` instance that connects to `self.dbname`.
        """
        return Db(dbname=self.sqlite_dbname, verbose=self.verbose)

    def get_mail_params(self):
        return self.conf.get(srm.C_MAIL)

    def _validate_bucket(self):
        """
        Tries to create a `google.cloud.storage.bucket.Bucket` instance to ensure that we can
        connect to the bucket designated by `self.bucket_name`. If we can here, then a child process
        should also be able to when it needs to. While we could store the bucket instance in our own
        instance variable, it's probably not safe to share these amongst child processes, so better
        to let each child process make it's own bucket instance.
        """
        storage_client = storage.Client()
        # A `google.cloud.storage.bucket.Bucket` instance.
        self.client.get_bucket(self.bucket_name)

    def _cleanup(self, signum, frame):
        """
        Terminate all child processes. Normally this is called when a SIGTERM is caught

        Args:
            signum: Don't call explicitly. Only used internally when this method is serving as a
                handler for a specific type of signal in the funtion `signal.signal`.
            frame: Don't call explicitly. Only used internally when this method is serving as a
                handler for a specific type of signal in the funtion `signal.signal`.
        """
        signame = signal.Signals(signum).name
        msg = "{} caught signal {}. Preparing for shutdown.".format(self.monitor_name, signame)
        self.logger.error(msg)
        # Email notification
        self.send_mail(subject="Shutting down", body=msg)
        child_processes = psutil.Process().children()
        # Kill child processes by sending a SIGKILL.
        [c.kill() for c in child_processes] # equiv. to os.kill(pid, signal.SIGKILL) on UNIX.
        self.sqlite_conn.conn.close()
        sys.exit(128 + signum)

    def _workflow(self, state, run_name):
        """
        Runs the workflow. Knows which stages to run, which is useful if the workflow needs to
        be rerun from a particular point.

        This method is meant to serve as the value of the `target` parameter in a call to
        `multiprocessing.Process`, and is not meant to be called directly by users of this library.

        Args:
            state: `multiprocessing.Queue` instance.
            run_name: `str`. The name of a sequencing run.
        """
        sl = self.get_sqlite_conn()
        rec = sl.get_run(run_name)
        if not rec[Db.TASKS_TARFILE]:
            self.task_tar(state=state, run_name=run_name, sqlite_conn=sl)
        if not rec[Db.TASKS_GCP_TARFILE]:
            self.task_upload(state=state, run_name=run_name, sqlite_conn=sl)
        sl.conn.close()

    def firestore_update_status(self, run_name, status):
        """
        This method only has an effect if Firestore is configured for use.
        Updates the status of a Firestore record; creates its own connection to the
        Firestore database since child processes can call this method; hence, it does not use
        `self.firestore_connection`.
        """
        if not self.firestore_collection:
            return
        firestore_coll = self.get_firestore_conn()
        firestore_payload = {
            srm.FIRESTORE_ATTR_WF_STATUS: status
        }
        self.logger.info("Firestore: Set {} status to {}.".format(run_name, status))
        firestore_coll.document(run_name).update(firestore_payload)

    def task_tar(self, state,  run_name, sqlite_conn):
        """
        Creates a gzip tarfile of the run directory and updates the Firestore record's status to
        indicate that this task is running. The tarfile will be created in the calling directory
        and named the same as the `run_name` parameter, but with a .tar.gz suffix.

        Once tarring is complete, the local database record is updated such that the attribute
        `sqlite_utils.Db.TASKS_TARFILE` is set to the path of the tarfile. Note that this method
        also updates the local database record to set the pid field with the process ID its running
        in.

        Args:
            state: `multiprocessing.Queue` instance.
            run_name: `str`. The name of a sequencing run.
            sqlite_conn: `sqlite3.Connection` instance for the local SQLite database.
        """
        try:
            sqlite_conn.update_run(name=run_name, payload={Db.TASKS_PID: os.getpid()})
            tarball_name = run_name + ".tar"
            self.logger.info("Tarring sequencing run {}.".format(run_name))
            # Update status of Firestore record
            self.firestore_update_status(run_name=run_name, status=Db.RUN_STATUS_TARRING)
            rec = sqlite_conn.get_run(run_name)
            run_path = rec[Db.TASKS_RUNDIR_PATH]
            tarball = utils.tar(run_path, tarball_name)
            sqlite_conn.update_run(name=run_name, payload={Db.TASKS_TARFILE: tarball_name})
            # Update status of Firestore record
            self.firestore_update_status(run_name=run_name, status=Db.RUN_STATUS_TARRING_COMPLETE)
        except Exception as e:
            state.put((run_name, os.getpid(), e))
            # Let child process terminate as it would have so this error is spit out into
            # any potential downstream loggers as well. This does not effect the main thread.
            raise

    def task_upload(self, state, run_name, sqlite_conn):
        """
        Uploads the tarred run dirctory to GCP Storage in the directory specified by `self.bucket_basedir`.
        The Firestore record's status is also updated to indicate that this task is running.
        The blob is named as $basedir/run_name/tarfile, where run_name is the squencing run name,
        and tarfile is the name of the tarfile produced by `self.task_tar`.

        Once uploading is complete, the local database record is updated such that the attribute
        `sqlite_utils.Db.TASKS_GCP_TARFILE` is set to the location of the blob as a string value
        formatted as '$bucket_name/blob_path'.
        Note that this method also updates the local database record to set the pid field with
        the process ID its running in.

        Finally, the local tarfile is removed.

        Args:
            state: `multiprocessing.Queue` instance.
            run_name: `str`. The name of a sequencing run.
            sqlite_conn: `sqlite3.Connection` instance for the local SQLite database.

        Raises:
            `sruns_monitor.exceptions.MissingTarfile`: There isn't a tarfile for this run (based on the record information
            in the SQLite database.
        """
        try:
            sqlite_conn.update_run(name=run_name, payload={Db.TASKS_PID: os.getpid()})
            rec = sqlite_conn.get_run(run_name)
            tarfile = rec[Db.TASKS_TARFILE]
            if not tarfile:
                raise srm_exceptions.MissingTarfile("Run {} does not have a tarfile.".format(run_name))
            # Upload tarfile to GCP bucket
            blob_name = self.create_blob_name(run_name=run_name, filename=tarfile)
            storage_client = storage.Client()
            # A `google.cloud.storage.bucket.Bucket` instance.
            bucket = storage_client.get_bucket(self.bucket_name)
            self.logger.info("Uploading {} to GCP Storage bucket {} as {}.".format(tarfile,self.bucket_name, blob_name))
            # Update status of Firestore record
            self.firestore_update_status(run_name=run_name, status=Db.RUN_STATUS_UPLOADING)
            utils.upload_to_gcp(bucket=bucket, blob_name=blob_name, source_file=tarfile)
            bucket_blob_path = "/".join([self.bucket_name, blob_name])
            sqlite_conn.update_run(
                name=run_name,
                payload={Db.TASKS_GCP_TARFILE: bucket_blob_path})
            # Remove local tarfile
            os.remove(tarfile)
            # Update status of Firestore record
            self.firestore_update_status(run_name=run_name, status=Db.RUN_STATUS_UPLOADING_COMPLETE)
        except Exception as e:
            state.put((run_name, os.getpid(), e))
            # Let child process terminate as it would have so this error is spit out into
            # any potential downstream loggers as well. This does not effect the main thread.
            raise

    def create_blob_name(self, run_name, filename):
        """
        Creates a name for a blob object to be in GCP. The name is formulated as follows:

            self.bucket_basedir + '/' + run_name + '/' + os.path.basename(filename)

        There will not be a '/' at the start.
        """
        return "/".join([self.bucket_basedir, run_name, os.path.basename(filename)]).lstrip("/")

    def kill_childprocess_if_running_to_long(self, pid):
        """
        Args:
            pid: `int`. The process ID of a child process.

        Returns:
            `Boolean`. `True` if the process was killed (kill signal sent) False otherwise.
        """
        process = utils.get_process(pid)
        if process:
            if utils.running_too_long(process, self.process_runtime_limit_sec):
                self.logger.info("Killing process {} for running too long".format(pid))
                process.kill()
                return True
                # The next iteration of the monitor will see that the pid isn't running and restart
                # the workflow if it hasn't finished yet.

    def get_rundir_path(self, run_name):
        rec = self.sqlite_conn.get_run(run_name)
        return rec[Db.TASKS_RUNDIR_PATH]

    def archive_run(self, run_name):
        """
        Moves the run directory to the completed runs directory.
        """
        from_path = self.get_rundir_path(run_name)
        self.logger.info("Moving run {run} to completed runs location {loc}.".format(run=run_name, loc=self.completed_runs_dir))
        shutil.move(from_path, self.completed_runs_dir)

    def process_new_run(self, run):
        """
        Creates a new record into the local sqlite db as well as the Firestore db.
        If mail is configured, sends an email notification about the new run first. 
        Then, initiates the workflow. 

        Before any of this happens, however, there is a check to ensure that the Illumina 
        Universal Copy Services (UCS) has had ample time to complete once the sentinal file appears
        in the output folder. Illumina Support recommends that this be 15 minutes, but this is 
        configurable in this program's JSON config file. 

        Args:
            run: `str`. Path to a run directory.
        """
        # Make sure that the sentinal file, i.e. CopyComplete.txt, is at least self.sentinal_file_age_minutes
        # old prior to processing:
        minutes_old = 0
        for sentinal_file_name in self.SENTINAL_FILES:
            sentinal_file_path = os.path.join(run, sentinal_file_name)
            if os.path.exists(sentinal_file_path):
                # One of the sentinal files will exist at this point in the program, otherwise this
                # method would never have been called. 
                minutes_old = utils.get_time_since_ctime(sentinal_file_path)
                break
        if not minutes_old > self.sentinal_file_age_minutes:
            self.logger.info("The sentinal file for run {} should be at least {} minutes old before processing starts. Will try again on next smon iteration".format(run, self.sentinal_file_age_minutes))
            return
        run_name = os.path.basename(run)
        self.send_mail(subject="New run {}".format(run_name), body=run_name)
        self.sqlite_conn.insert_run(rundir_path=run)
        # Create Firestore document
        firestore_coll = self.get_firestore_conn()
        if firestore_coll:
            firestore_payload = {
                srm.FIRESTORE_ATTR_RUN_NAME: run_name,
                srm.FIRESTORE_ATTR_WF_STATUS: Db.RUN_STATUS_STARTING
            }
            self.logger.info("Firestore: new run {}".format(run_name))
            firestore_coll.document(run_name).set(firestore_payload)
        self.run_workflow(run_name)

    def process_completed_run(self, run_name, archive=True):
        """
        Moves the run directory to the completed runs directory location that is defined
        by `sruns_monitor.C_COMPLETED_RUNS_DIR`.

        Updates Firestore to set

            * the GCP storage attribute (identified by the variable `sruns_monitor.FIRESTORE_ATTR_STORAGE`)
              to the location of the gzip tarfile of the run directory in GCP bucket storage. This
              value is extracted from the local record in the SQLite database, and is formatted as
              '$bucket_name/blob_path'.
            * the workflow status attribute (identified by the variable `sruns_monitor.FIRESTORE_ATTR_WF_STATUS`.
              to completed.

        Args:
            run_name: `str`.
            archive: `boolean`. True meas to move the run directory to the completed runs location.

        """
        rec = self.sqlite_conn.get_run(run_name)
        if archive:
            self.archive_run(run_name)
        # Update Firestore record
        firestore_conn = self.get_firestore_conn()
        if firestore_conn:
            firestore_payload = {
                srm.FIRESTORE_ATTR_WF_STATUS: Db.RUN_STATUS_COMPLETE,
                srm.FIRESTORE_ATTR_STORAGE: rec[Db.TASKS_GCP_TARFILE]
            }
            self.logger.info("Firestore: Update run record {} with {}.".format(run_name, firestore_payload))
            firestore_conn.document(run_name).update(firestore_payload)
        self.send_mail(subject="Finished processing run {}".format(run_name), body=run_name)

    def run_workflow(self, run_name):
        p = Process(target=self._workflow, args=(self.state, run_name))
        p.start()

    def scan(self):
        """
        Finds all sequencing runs in `self.watchdirs` that are finished sequencing.

        Returns:
            `list`. Each element is the path to a run directory.
        """
        run_paths = []
        for path in self.watchdirs:
            for run_name in os.listdir(path):
                run_path = os.path.join(path,run_name)
                if not os.path.isdir(run_path):
                    continue
                if set(os.listdir(run_path)).intersection(self.SENTINAL_FILES):
                    # This is a completed run directory
                    run_paths.append(run_path)
        return run_paths

    def process_rundirs(self, runs):
        """
        For each sequencing run name, checks it's status with regard to the workflow and initiates
        any remaining steps, i.e. restart, cleanup, ...

        Args:
            runs: `list` where each element is the path to a run directory.
        """
        for run in runs:
            run_name = os.path.basename(run)
            self.logger.info("Processing rundir {}".format(run_name))
            run_status = self.sqlite_conn.get_run_status(run_name)
            if run_status == Db.RUN_STATUS_NEW:
                self.process_new_run(run)
            elif run_status == Db.RUN_STATUS_COMPLETE:
                self.process_completed_run(run_name)
            elif run_status == Db.RUN_STATUS_RUNNING:
                # Check if it has been running for too long.
                rec = self.sqlite_conn.get_run(run_name)
                pid = rec[Db.TASKS_PID]
                if self.kill_childprocess_if_running_to_long(pid):
                    msg = "Child process {} for run {} killed for running too long.".format(pid, run_name)
                    self.logger.info(msg)
                    # Send email notification
                    self.send_mail(subject="Run {} killed".format(run_name), body=msg)
            elif run_status == Db.RUN_STATUS_NOT_RUNNING:
                self.run_workflow(run_name)


    def send_mail(self, subject, body):
        """
        Sends an email if the mail parameters are provided in the configuration.  
        Prior to sending an email, the subject and body of the email will be logged. 

        Args:
            subject: `str`. The email's subject. Note that the subject will be mangled a bit - 
                it will be prefixed with `self.monitor_Name` plus a colon and a space. 
            body: `str`. The email body w/o any markup.

        Returns: `None`. 
        """
        subject = self.monitor_name + ": " + subject
        mail_params = self.get_mail_params()
        if not mail_params:
            return
        from_addr = mail_params["from"]
        host = mail_params["host"]
        tos = mail_params["tos"]
        self.logger.info("""
            Sending mail
            Subject: {}
            Body: {}
            """.format(subject, body))
        utils.send_mail(from_addr=from_addr, to_addrs=tos, subject=subject, body=body, host=host)

    def start(self):
        cycle_num = 0
        try:
            while True:
                cycle_num += 1
                self.logger.info("Cycle {}".format(cycle_num))
                # Remove any zombie processes
                # Curious why or how this works? See book Programming Python, 4th ed. section
                # "Killing the zombies: Don't fear the reaper!".
                try:
                    os.waitpid(0, os.WNOHANG)
                    # The 0 argument above means to check for any completed child process, not one with a
                    # specific pid.
                except ChildProcessError:
                    pass # No child processes
                finished_rundirs = self.scan()
                self.process_rundirs(runs=finished_rundirs)
                # Now check the shared queue object to see if any child process ran into some trouble
                # and recorded its dying last words:
                child_process_msg = None
                try:
                    child_process_msg = self.state.get(block=False)
                except queue.Empty:
                    pass
                if child_process_msg:
                    run_name = child_process_msg[0]
                    pid = child_process_msg[1]
                    err_msg = child_process_msg[2]
                    msg = "Run {} with process ID {} exited with message '{}'.".format(run_name, pid, err_msg)
                    self.logger.error(msg)
                    self.logger.info("Sending email notification")
                    self.send_mail(subject="Error for run {}".format(run_name), body=msg)
                deleted_dirs = utils.clean_completed_runs(basedir=self.completed_runs_dir, limit=self.sweep_age_sec)
                if deleted_dirs:
                    for d_path in deleted_dirs:
                        self.logger.info("Deleted directory {}".format(d_path)) 
                time.sleep(self.cycle_pause_sec)
        except Exception as e:
            tb = e.__traceback__
            tb_msg = pformat(traceback.extract_tb(tb).format())
            msg = "Main process Exception: {} {}".format(e, tb_msg)
            self.logger.error(msg)
            self.send_mail(subject="Error", body=msg)
            raise


### Example
# m = Monitor(conf_file="my_conf_file.json")
# m.start()
###
