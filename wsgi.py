import logging

from ap_server.server import app

# logging
logging.getLogger('ap_server').setLevel(logging.DEBUG)

FORMAT = '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'  # by default funcName is removed
# FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('SOFTWAY4IoT-APServer')
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    app.run()
