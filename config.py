import os
PROPAGATE_EXCEPTIONS = True
basedir = os.path.abspath(os.path.dirname(__file__))
if os.environ.get("OPENSHIFT_DATA_DIR") == None:
    DATADIR = os.path.join(basedir,"data")
else:
    DATADIR = os.environ.get("OPENSHIFT_DATA_DIR")

if os.environ.get("OPENSHIFT_MONGODB_DB_HOST") != None:
    MONGODB_HOST = os.environ.get["OPENSHIFT_MONGODB_DB_HOST"]
else:
    MONGODB_HOST = "192.168.1.8"

MONGODB_SETTINGS = {
    'DB': "nodeclassifier",
    'host': MONGODB_HOST
}
