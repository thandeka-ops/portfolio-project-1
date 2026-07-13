from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": os.getenv("APP_NAME", "Flask DevOps Portfolio"),
        "environment": os.getenv("APP_ENV", "Development"),
        "status": "Running Successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/version")
def version():
    return jsonify({
        "application": os.getenv("APP_NAME", "Flask DevOps Portfolio"),
        "version": "1.0.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)