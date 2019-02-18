import logging

from flask import Flask, request
from flask.json import jsonify
from marshmallow import ValidationError

from ap_server.common.schemas import CreateApSchema
from ap_server.helper.create_ap_helper import CreateApHelper as ap_helper

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/ap_running", methods=['GET'])
def get_ap_running():
    ap_running = ap_helper.list_ap_running()
    logger.info("Ap running: {}".format(ap_running))
    return jsonify({"data": ap_running})


@app.route("/stop_ap/<string:ap_name>", methods=['DELETE'])
def stop_ap(ap_name):
    logger.info("Stop AP {}".format(ap_name))
    status = ap_helper.stop_ap(ap_name)
    logger.info("AP {} stop: {}".format(ap_name, status))
    return jsonify({"data": status})


@app.route("/create_ap", methods=['POST'])
def create_ap():
    try:
        ap = CreateApSchema().load(request.json)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 422

    logger.info("Create AP: {}".format(ap.to_dict()))
    try:
        status = ap_helper.create_ap(**ap.to_dict())
        logger.info("AP created {}".format(status))
        return jsonify({"data": status})
    except Exception as e:
        logger.error(e)
        return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
