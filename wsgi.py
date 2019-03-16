import logging

from ap_server.server import app

# logging
logging.getLogger('ap_server').setLevel(logging.DEBUG)

if __name__ == "__main__":
    # Run application server
    app.run()
