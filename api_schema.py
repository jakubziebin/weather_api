from __future__ import annotations

from typing import Any
from datetime import datetime

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
        """input data must be in json format: {'TEMPERATURE': value}, id and date will be given automatically"""
        connection = connect_to_db()
        cursor = connection.cursor() 
        request_data = request.get_json()
        date_to_db = datetime.today().strftime('%Y-%m-%d')

        request_data["DATE"] = date_to_db
        
        try:
            Temparature(**request_data)
        except ValidationError as error:
            raise ValidationError("Something is wrong with this parameters from arduino!") from error
        
        query = "INSERT INTO TEMPERATURE(TEMPERATURE, DATE) VALUES(%(TEMPERATURE)s, %(DATE)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
        return "done", 201
    else:
        """Value return from database should look like this: {'ID': id, 'TEMPERATURE': value, 'DATE': requested_date}"""
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        request_data = request.get_json()
        
        query = "SELECT * FROM TEMPERATURE WHERE ID = %(ID)s AND DATE = %(DATE)s"
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
        """input data must be in json format: {'HUMIDITY': value}, id and date will be given automatically"""
        connection = connect_to_db()
        cursor = connection.cursor()
        request_date = request.get_json()
        date_to_db = datetime.today().strftime('%Y-%m-%d')

        request_date["DATE"] = date_to_db

        try:
            Humidity(**request_date)
        except ValidationError as error:
            raise ValidationError("Something is wrong with this parameters !") from error
        
        query = "INSERT INTO HUMIDITY(HUMIDITY, DATE) VALUES(%(HUMIDITY)s, %(DATE)s)"
        cursor.execute(query, request_date)
        connection.commit()

        connection.close()
        return "done", 201
    else:
        """Value return from database should look like this: {'ID': id, 'HUMIDITY': value, 'DATE': requested_date}"""
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        request_data = request.get_json()
        
        query = "SELECT * FROM HUMIDITY WHERE ID = %(ID)s AND DATE = %(DATE)s"
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
        """input data must be in json format: {'PARTICLES': value}, id and date will be given automatically"""
        connection = connect_to_db()
        cursor = connection.cursor()
        request_data = request.get_json()
        date_to_db = datetime.today().strftime('%Y-%m-%d')

        request_data["DATE"] = date_to_db

        try:
            Particles(**request_data)
        except ValidationError as error:
            raise ValidationError("Something is wrong with this parameters !") from error
        
        query = "INSERT INTO PARTICLES(PARTICLES, DATE) VALUES(%(PARTICLES)s, %(DATE)s)"
        cursor.execute(query, request_data)
        connection.commit()

        connection.close()
        return "done", 201
    else:
        """Value return from database should look like this: {'ID': id, 'PARTICLES': value, 'DATE': requested_date}"""
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        request_data = request.get_json()
        
        query = "SELECT * FROM PARTICLES WHERE ID = %(ID)s AND DATE = %(DATE)s"
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
