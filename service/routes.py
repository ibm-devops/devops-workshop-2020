from flask import jsonify
from service import app

counter = 0

@app.route("/")
def index():
    """ Inde xURL """
    return "Hello from Flask"

@app.route("/counter", methods=["GET"])
def get_counter():
    """ Get counter """
    global counter
    counter += 1
    return jsonify(counter=counter)

def rest_counter():
    global counter
    if app.testing:
        counter = 0