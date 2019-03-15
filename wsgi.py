import logging

from ap_server.common.utils import create_symlink
from ap_server.server import app

# logging
logging.getLogger('ap_server').setLevel(logging.DEBUG)

# Create symbolic link to application socket
create_symlink()

if __name__ == "__main__":
    # Run application server
    app.run()
