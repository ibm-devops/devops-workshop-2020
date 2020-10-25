from flask import jsonify
from service import app

counter = 0

@app.route("/")
def index():
    return "Hello from Flask"

@app.route("/counter")
def get_counter():
    global counter
    counter += 1
    return jsonify(counter=counter)


def reset_counter():
    global counter
    if app.testing:
        counter = 0
