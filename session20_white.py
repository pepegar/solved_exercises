from flask import Flask, jsonify

server = Flask("calculator")

@server.route("/sum/<operand1>/<operand2>")
def sum_handler(operand1, operand2):
    return jsonify(int(operand1) + int(operand2))

server.run()