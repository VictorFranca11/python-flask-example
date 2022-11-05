from flask import Flask, Response
import os

app = Flask(__name__)

contador = 0

@app.route("/")
def hello_world():
    return "ola mundo"

@app.route("/health")
def health():
    return Response("ok", status=200)

@app.route("/counter")
def counter():
    global contador
    contador += 1
    return str(contador)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ["APP_PORT"], debug=True)
