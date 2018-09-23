import os

from flask import Flask, jsonify, render_template
from flask_basicauth import BasicAuth

from newsbeuter_spread.db import DB


app = Flask(__name__)
app.config["BASIC_AUTH_USERNAME"] = os.environ.get("USERNAME", None)
app.config["BASIC_AUTH_PASSWORD"] = os.environ.get("PASSWORD", None)
app.config["BASIC_AUTH_FORCE"] = bool(os.environ.get("AUTH", "False"))
basic_auth = BasicAuth(app)
db = DB()


@app.route("/")
def index():
    items = list(db.get_unread())
    return render_template("index.html", items=items)


@app.route("/api/item/")
def items():
    items = [item.__dict__ for item in db.get_unread()]
    return jsonify({"status": "success", "items": items})


@app.route("/api/item/<id>/", methods=["DELETE"])
def delete(id):
    db.mark_read(id)
    return jsonify({"status": "success"})
