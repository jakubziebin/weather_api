from __future__ import annotations

from typing import Any

from flask import Flask
from flask import jsonify
from flask import request
from mysql import connector 


def connect_to_db():
    connection = connector.connect(
        user = "student",
        password = "Student123",
        host = "127.0.0.1",
        database = "projekt_air",
        auth_plugin = "mysql_native_password"
    )
    return connection


app = Flask(__name__)


@app.route('/temperature', methods=['GET', 'POST'])
def temperature() -> dict[Any] | None:
    if request.method == 'POST':
        connection = connect_to_db()
        cursor = connection.cursor()
        request_data = request.get_json()

        query = "INSERT INTO TEMPERATURE(TEMPERATURE) VALUES(%(TEMPERATURE)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
        return "done", 201
    else:
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM TEMPERATURE")
        
        connection.close()


@app.route('/humidity', methods=['GET', 'POST'])
def get_humidity() -> dict[Any] | None:
    if request.method == 'POST':
        connection = connect_to_db()
        cursor = connection.cursor()
        request_data = request.get_json()

        query = "INSERT INTO HUMIDITY(HUMIDITY, DATE_TIME) VALUES (%(HUMIDITY)s, %(DATE_TIME)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
    else:
        connection = connect_to_db()
        cursor =connection.cursor(dictionary=True)
        
        query = "SELECT * FROM HUMIDITY"
        cursor.execute(query)
        
        connection.close()


@app.route('/particles', methods=['GET', 'POST'])
def get_particles() -> dict[Any] | None:
    if request.method == 'POST':
        connection = connect_to_db()
        cursor = connection.cursor()
        request_data = request.get_json()

        query = "INSERT INTO PARTICLES(PARTICLES, DATE_TIME) VALUES (%(PARTICLES)s, %(DATE_TIME)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
    else:
        connection = connect_to_db()
        cursor =connection.cursor(dictionary=True)
        
        query = "SELECT * FROM PARTICLES"
        cursor.execute(query)

        connection.close


if __name__ == "__main__":
    app.debug = True
    app.run()
