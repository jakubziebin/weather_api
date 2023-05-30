from __future__ import annotations

from typing import Any

from flask import Flask
from flask import jsonify
from flask import request
from pydantic import ValidationError

from connect_db import connect_to_db
from response_schemas import Temparature, Humidity, Particles

app = Flask(__name__)


@app.route('/temperature', methods=['GET', 'POST'])
def temperature() -> dict[Any] | None:
    if request.method == 'POST':
        """input data must be in json format: {'TEMPERATURE': value}, id will be given automatically"""
        connection = connect_to_db()
        cursor = connection.cursor() 
        request_data = request.get_json()

        try:
            Temparature(**request_data)
        except ValidationError as error:
            raise ValidationError("Something is wrong with this parameters !") from error
        
        query = "INSERT INTO TEMPERATURE(TEMPERATURE) VALUES(%(TEMPERATURE)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
        return "done", 201
    else:
        """Value return from database should look like this: {'ID': id, 'TEMPERATURE': value}"""
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        request_data = request.get_json()
        
        query = "SELECT ID, TEMPERATURE FROM TEMPERATURE WHERE ID = %(ID)s"
        cursor.execute(query, request_data)
        result = cursor.fetchone()

        try:
            return_value = Temparature(**result)
        except ValidationError as error:
            raise ValidationError("something is wrong with values from db !") from error
        connection.close()
        return return_value.json()


@app.route('/humidity', methods=['GET', 'POST'])
def humidity() -> dict[Any] | None:
    if request.method == 'POST':
        """input data must be in json format: {'HUMIDITY': value}, id will be given automatically"""
        connection = connect_to_db()
        cursor = connection.cursor()
        request_data = request.get_json()

        try:
            Humidity(**request_data)
        except ValidationError as error:
            raise ValidationError("Something is wrong with this parameters !") from error
        
        query = "INSERT INTO HUMIDITY(HUMIDITY) VALUES(%(HUMIDITY)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
        return "done", 201
    else:
        """Value return from database should look like this: {'ID': id, 'HUMIDITY': value}"""
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        request_data = request.get_json()
        
        query = "SELECT ID, HUMIDITY FROM HUMIDITY WHERE ID = %(ID)s"
        cursor.execute(query, request_data)
        result = cursor.fetchone()

        try:
            return_value = Humidity(**result)
        except ValidationError as error:
            raise ValidationError("something is wrong with values from db !") from error
        connection.close()
        return return_value.json()


@app.route('/particles', methods=['GET', 'POST'])
def particles() -> dict[Any] | None:
    if request.method == 'POST':
        """input data must be in json format: {'PARTICLES': value}, id will be given automatically"""
        connection = connect_to_db()
        cursor = connection.cursor()
        request_data = request.get_json()

        try:
            Particles(**request_data)
        except ValidationError as error:
            raise ValidationError("Something is wrong with this parameters !") from error
        
        query = "INSERT INTO PARTICLES(PARTICLES) VALUES(%(PARTICLES)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
        return "done", 201
    else:
        """Value return from database should look like this: {'ID': id, 'PARTICLES': value}"""
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        request_data = request.get_json()
        
        query = "SELECT ID, PARTICLES FROM PARTICLES WHERE ID = %(ID)s"
        cursor.execute(query, request_data)
        result = cursor.fetchone()

        try:
            return_value = Particles(**result)
        except ValidationError as error:
            raise ValidationError("something is wrong with values from db !") from error
        connection.close()
        return return_value.json()


if __name__ == "__main__":
    app.debug = True
    app.run()
