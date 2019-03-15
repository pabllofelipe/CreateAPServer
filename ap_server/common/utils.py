import errno
import logging
import os

OPT_PREFIX = '/opt/sw4iot/CreateAPServer'
RUN_PREFIX = '/run/sw4iot'
SRC_AP_SERVER_SOCK = '{}/sw4iot_ap_server.sock'.format(OPT_PREFIX)
DST_AP_SERVER_SOCK = '{}/sw4iot_ap_server.sock'.format(RUN_PREFIX)

logger = logging.getLogger(__name__)


def create_symlink():
    """
    Create symbolic link to application
    """
    logger.debug("Create directories")
    mkdirs(RUN_PREFIX)
    logger.debug("Create symbolic link")
    os.system("ln -s {} {}".format(SRC_AP_SERVER_SOCK, DST_AP_SERVER_SOCK))


def mkdirs(newdir):
    """
    Create directory

    :param newdir: Directory path
    :param mode:
    """
    try:
        os.makedirs(newdir)
    except OSError as err:
        # Reraise the error unless it's about an already existing directory
        if err.errno != errno.EEXIST or not os.path.isdir(newdir):
            raise
