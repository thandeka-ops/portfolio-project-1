import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Flask DevOps Portfolio")
APP_ENV = os.getenv("APP_ENV", "Development")


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "environment": APP_ENV,
        "status": "Running Successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)