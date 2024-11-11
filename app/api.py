import http.client
from flask import Flask, jsonify
import math

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}

def check_types(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Parameters must be numbers")

@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"

@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de potencia
@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.power(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de raíz cuadrada
@api_application.route("/calc/square_root/<op_1>", methods=["GET"])
def square_root(op_1):
    try:
        num = util.convert_to_number(op_1)
        if num < 0:
            return ("Square root of a negative number is undefined in the real number domain.", http.client.BAD_REQUEST, HEADERS)
        return ("{}".format(CALCULATOR.square_root(num)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


# Ruta para el logaritmo en base 10
@api_application.route("/calc/log_base_10/<op_1>", methods=["GET"])
def log_base_10(op_1):
    try:
        num = util.convert_to_number(op_1)
        if num <= 0:
            return ("Logarithm of zero or a negative number is undefined.", http.client.BAD_REQUEST, HEADERS)
        return ("{}".format(CALCULATOR.log_base_10(num)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

