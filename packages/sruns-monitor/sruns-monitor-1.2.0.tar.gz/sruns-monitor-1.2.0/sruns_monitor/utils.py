# -*- coding: utf-8 -*-

from email.message import EmailMessage
import json
import jsonschema
import os
import psutil
from smtplib import SMTP, SMTPException
import shutil
import subprocess
import tarfile
import time

import sruns_monitor as srm


def create_subprocess(cmd, check_retcode=True):                                                        
    """Runs a command in a subprocess and checks for any errors.                                       
                                                                                                       
    Creates a subprocess via a call to ``subprocess.Popen`` with the argument ``shell=True``, and pipes
    stdout and stderr.                                                                                 
                                                                                                       
    Args:                                                                                              
        cmd: `str`. The command to execute.                                                            
        check_retcode: `bool`. When `True`, then a ``subprocess.SubprocessError`` is raised when the
          subprocess returns a non-zero return code.                                                   
          The error message will display the command that was executed along with its                  
          actual return code,  as well as any messages that the subprocess sent to STDOUT and STDERR.
          When `False`, the ``subprocess.Popen`` instance will be returned instead and it is expected
          that the caller will call its ``communicate`` method.                                        
                                                                                                       
    Returns:                                                                                           
        Two-item tuple containing the subprocess's STDOUT and STDERR streams' content if               
        ``check_retcode=True``, otherwise a ``subprocess.Popen`` instance.                             
                                                                                                       
    Raises:                                                                                            
        subprocess.SubprocessError: There is a non-zero return code and ``check_retcode=True``.        
    """                                                                                                
    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)          
    if check_retcode:                                                                                  
        stdout, stderr = popen.communicate()                                                           
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        retcode = popen.returncode                                                                     
        if retcode:                                                                                    
            # subprocess.SubprocessError was introduced in Python 3.3.                                 
            errmsg = f"subprocess command '{cmd}' failed with returncode '{retcode}'.\n\nstdout is: '{stdout}'.\n\nstderr is: '{stderr}'."
            raise subprocess.SubprocessError(errmsg)
        return stdout, stderr                                                                          
    else:                                                                                              
        return popen 


def validate_conf(conf_file, schema_file):
    """
    Ensures that the configuration file is valid according to the internal schema. Before
    validating, any keys that start with '#' will be removed from the JSON object.

    Args:
        conf_file: `str`. The JSON configuration file.
        schema_file: `str`. The JSON schema file.
    """
    conf_fh = open(conf_file)
    jconf = json.load(conf_fh)
    conf_fh.close()
    # Remove any keys that have been commented out
    for key in list(jconf.keys()):
        if key.startswith("#"):
            jconf.pop(key)
    schema_fh = open(schema_file)
    jschema = json.load(schema_fh)
    schema_fh.close()
    jsonschema.validate(jconf, jschema)
    return jconf

def clean_completed_runs(basedir, limit):
    """
    Removes directories (i.e run or analysis directories) within the specified base directory 
    that haven't been modified since the specified number of seconds. 

    Args:
        basedir: `str`. The directory path in which to scan for directories that are older than
            the specified number of seconds in the `limit` parameter. 
        limit: `int`. The number of seconds

    Returns:
        `list` of deleted directories.
    """
    deleted_dirs = []
    for d in os.listdir(basedir):
        d_path = os.path.join(basedir, d)
        if delete_directory_if_too_old(dirpath=d_path, age_seconds=limit):
            deleted_dirs.append(d_path)
    return deleted_dirs



def tar(input_dir, tarball_name, compress=False):
    """
    Creates a tar.gz tarball of the provided directory and returns the tarball's name.
    The tarball's name is the same as the input directory's name, but with a .tar.gz extension.

    Args:
        input_dir: `str`. Path to the directory to tar up.
        tarball_name: `str`. Name of the output tarball.
        compress: `boolean`. True enables gzip compression. Not recommended with the latest types of
            Illumina runs, i.e. NovaSeq, since the files are mostly binary which isn't compressible.
            For example, I compressed a 428 GB NovaSeq run with 'tar -zcf' and the output was 422 GB.

    Returns:
        `None`.
    """
    mode = 'w'
    if compress:
        mode = "w:gz"
    with tarfile.open(tarball_name, mode=mode) as tb:
        tb.add(name=input_dir, arcname=os.path.basename(input_dir))

def extract(filename, where):
   """
   Extracts a tar file.

   Args:
       filename: `str`. Local filepath of the file to extract.
       where: `str`. The local directory path in which `filename` will be extracted.

   Returns:
       `None`.
   """
   tf = tarfile.open(filename)
   tf.extractall(path=where)

def upload_to_gcp(bucket, blob_name, source_file):
    """
    Uploads a local file to GCP storage in the specified bucket.

    Args:
        bucket: `google.cloud.storage.bucket.Bucket` instance, which can be created like so::

            from google.cloud import storage
            storage_client = storage.Client()
            bucket = storage_client.get_bucket("my_bucket_name")

        blob_name: `str`. The name to give the uploaded file in the bucket.
        source_file: `str`. The name of the local file to upload.

    Returns:
        `None`.

    Raises:
        `FileNotFoundError`: source_file was not locally found.
    """
    blob = bucket.blob(blob_name)
    return blob.upload_from_filename(source_file)

def get_process(pid):
    """
    Args:
        pid: `int`. The process ID of a process.

    Returns:
        `psutil.Process`: There is a process that exists in the system process table.
        `None`: There is not a process that exists in the system process table.
    """
    try:
        process = psutil.Process(pid)
        return process
    except psutil.NoSuchProcess:
        return None

def running_too_long(process, limit_seconds=None):
    """
    Indicates whether a process has been running longer than a specified amount of time
    in seconds.

    Args:
       process: `psutil.Process` instance.
       limit_seconds: `int`. Number of seconds. If the process has
           been running longer than this amount of seconds, this function will return True.

    Returns:
        `boolean`.
    """
    if not limit_seconds:
        return False
    created_at = process.create_time() # Seconds since epoch
    process_age = (time.time() - created_at)
    if process_age > limit_seconds:
        return True
    return False

def get_file_age(filepath):
    """
    Returns the age of the file in seconds.
    """
    now = time.time() # seconds since epoch
    file_mtime = os.path.getmtime(filepath)
    return now - file_mtime


def get_time_since_ctime(filepath):
    """
    Gets the difference, in minutes, of the current time minus the specified file's inode change
    time (ctime, for metadata modification). This is useful for determinig how long a file as been
    copied over to NFS since - the mtime and atime timestamps are preservered from the copy source,
    but the ctime in this sense reveals when the file was copied to NFS since the file permissions
    changed at that point in time.

    Returns:
        `float`.
    """
    ctime = os.path.getctime(filepath)
    now_time = time.time() # seconds since the epoch
    diff_minutes = (now_time - ctime)/60.0
    return diff_minutes

def delete_directory_if_too_old(dirpath, age_seconds):
    """
    Removes the directory, or file, if it hasn't been modified  since the specified number of seconds.

    Args:
        dirpath: `str`. The directory (or faile) to remove. 
        age_seconds: `int`. If the modification time of the directory/file is more >= this many
            seconds, it will be deleted.

    Returns:
        `boolean`: True means that the directory was removed.
    """
    if get_file_age(dirpath) >= age_seconds:
        if os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
        else:
            os.remove(dirpath)
        return True
    return False

def send_mail(from_addr, to_addrs, subject, body, host):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg.set_content(body)
    with SMTP(host=host, timeout=5) as smtp:
        return smtp.send_message(msg=msg, from_addr=from_addr, to_addrs=to_addrs)
