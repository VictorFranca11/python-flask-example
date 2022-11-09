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

#docker build . -t app.flask:1.0.0
#docker build . -t app.flask:2.0.0
@app.route("/version")
def version():
    return "2.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ["APP_PORT"], debug=True)
