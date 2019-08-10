from flask import Blueprint, request, jsonify

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return jsonify({"msq": "hellow dooly"})
