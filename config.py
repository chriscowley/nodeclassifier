import os
PROPAGATE_EXCEPTIONS = True
basedir = os.path.abspath(os.path.dirname(__file__))
if os.environ.get("OPENSHIFT_DATA_DIR") == None:
    DATADIR = os.path.join(basedir,"data")
else:
    DATADIR = os.environ.get("OPENSHIFT_DATA_DIR")
