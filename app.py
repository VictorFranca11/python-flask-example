from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "ola mundo"

@app.route("/health")
def health():
    return Response("ok", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ["APP_PORT"], debug=True)
