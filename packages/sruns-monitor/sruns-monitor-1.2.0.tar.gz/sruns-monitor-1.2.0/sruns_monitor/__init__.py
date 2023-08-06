# -*- coding: utf-8 -*-

import logging
import os
import sys

import sruns_monitor.logging_utils

#: The log directory
LOG_DIR = "Logs_" + __package__.capitalize()
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

logger = logging.getLogger(__package__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(stream=sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging_utils.FORMATTER)
logger.addHandler(ch)
# Add debug file handler to the logger:
logging_utils.add_file_handler(logger=logger, log_dir=LOG_DIR, level=logging.DEBUG, tag="debug")
# Add error file handler to the logger:
logging_utils.add_file_handler(logger=logger, log_dir=LOG_DIR, level=logging.ERROR, tag="error")

#: The JSON Schema file that defines the properties of the configuration file.
CONF_SCHEMA = os.path.join(os.path.dirname(__file__), "schema.json")

#: The name of the monitor. The name will appear in the subject line if email notification is
#: configured, as well as in other places, i.e. log messages.
C_MONITOR_NAME = "name"

#: Configuration parameter names in conf.json. Each of the variables that starts with a `C_` denotes
#: a config parameter.
C_WATCHDIRS = "watchdirs"

#: JSON configuration parameter name for specifying the mail configuration object.
C_MAIL = "mail"

#: JSON configuration parameter name for specifying the location of the completed runs directory.
C_COMPLETED_RUNS_DIR = "completed_runs_dir"

#: How old in minutes the sentinal file, i.e. CopyComplete.txt, should be before initiating
#: any tasks, such as tarring the run directory. Illumina Support recommends 15 minutes, which
#: is thus the default. This helps to ensure that the Illumina Universal Copy Services (UCS) running
#: on the sequencer has had ample time to complete once the sentinal file appears.
C_SENTINAL_FILE_AGE_MINUTES = "sentinal_file_age_minutes"

#: JSON configuration parameter name for specifying how long a directory in the completed runs location
#: can exist for prior to being deleted.
C_SWEEP_AGE_SEC = "sweep_age_sec"

#: JSON configuration parameter name for specifying the name of the SQLite database.
C_SQLITE_DB = "sqlite_db"

#: JSON configuration parameter name for specifying the Firestore collection.
C_FIRESTORE_COLLECTION = "firestore_collection"

#: JSON configuration parameter name for specifying the Google Storage bucket name.
C_GCP_BUCKET_NAME = "gcp_bucket_name"

#: JSON configuration parameter name for specifying the folder to write to in the Google bucket.
C_GCP_BUCKET_BASEDIR = "gcp_bucket_basedir"

#: JSON configuration parameter name for specifying how long to pause between monitor scans.
C_CYCLE_PAUSE_SEC = "cycle_pause_sec"

#: JSON configuration parameter name for specifying how long a child prcocess can run.
C_TASK_RUNTIME_LIMIT_SEC = "task_runtime_limit_sec"

### Attribute names for Firestore database
FIRESTORE_ATTR_RUN_NAME = "name"

#: The status of the workflow. Possible values are provided by the
#: `sruns_monitor.monitor.Monitor.RUN_STATUS_*` attributes.
FIRESTORE_ATTR_WF_STATUS = "workflow_status"

#: Bucket storage object path for the tarred run directory in the form bucket_name/path/to/run.tar.gz.
FIRESTORE_ATTR_STORAGE = "storage"

#: Firestore database attribute name. Used when setting or getting the JSON serialization of 
#: a Pub/Sub message associated with this document.
FIRESTORE_ATTR_SS_PUBSUB_DATA = "samplesheet_pubsub_data"

#: Firestore database attribute name. Used when setting or getting the path to the demultiplexing
#: results folder in Google Storage.  This is the storage object path, prefixed with the bucket name.
FIRESTORE_DEMUX_PATH = "demux_storage"
