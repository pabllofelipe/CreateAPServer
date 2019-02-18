import json

from flask import Flask, request
from flask.json import jsonify

from ap_server.helper.create_ap_helper import CreateApHelper as ap_helper

app = Flask(__name__)


@app.route("/ap_running", methods=['GET'])
def get_ap_running():
    ap_running = ap_helper.list_ap_running()
    return jsonify({"data": ap_running})


@app.route("/stop_ap/<string:ap_name>", methods=['DELETE'])
def stop_ap(ap_name):
    status = ap_helper.stop_ap(ap_name)
    return jsonify({"data": status})


@app.route("/create_ap", methods=['POST'])
def create_ap():
    data = json.loads(request.json)
    try:
        status = ap_helper.create_ap(**data)
        return jsonify({"data": status})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')
