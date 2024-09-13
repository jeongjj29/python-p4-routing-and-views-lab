#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return parameter


@app.route("/count/<parameter>")
def count(parameter):
    count = "\n".join(str(i) for i in range(int(parameter))) + "\n"
    return count


@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "Invalid Operation"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
