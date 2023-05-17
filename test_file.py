from flask import Flask
from flask import jsonify
from flask import request
from typing import Any


app = Flask(__name__)


@app.route('/temperature', methods=['GET', 'POST'])
def get_temperature() -> dict[Any] | None:
    if request.method == 'POST':
        return jsonify(**request.json), 201
    else:
        return jsonify(result="test_temperature")



@app.route('/humidity', methods=['GET', 'POST'])
def get_humidity() -> dict[Any]:
    if request.method == 'POST':
        return jsonify(**request.json), 201
    else:
        return jsonify(result="test_humidity")


@app.route('/particles', methods=['GET', 'POST'])
def get_particles() -> dict[Any]:
    if request.method == 'POST':
        return jsonify(**request.json), 201
    else:
        return jsonify(result="test_particles")


if __name__ == "__main__":
    app.debug = True
    app.run()
