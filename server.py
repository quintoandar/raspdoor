import opendoor
import time

from flask import Flask, redirect
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get():
    header = "<html><head><style type='text/css'>@media only screen and (min-device-width : 320px) and (max-device-width : 480px) {input[type=submit] {width: Calc(100% - 20px); margin: auto 10px; height: 30%; font-size: 40pt} }</style></head>"
    return header + "<body><form action='/' method='POST'><input type='submit' value='Abrir porta'/></form></body></html>"

@app.route("/", methods=["POST"])
def post():
    opendoor.open()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0')