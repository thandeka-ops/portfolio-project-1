from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)


@app.route("/")
def home():
    logger.info("GET /")
    return jsonify({
        "application": os.getenv("APP_NAME", "Flask DevOps Portfolio"),
        "environment": os.getenv("APP_ENV", "Development"),
        "status": "Running Successfully"
    })


@app.route("/health")
def health():
    logger.info("GET /health")
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/version")
def version():
    logger.info("GET /version")
    return jsonify({
        "application": os.getenv("APP_NAME", "Flask DevOps Portfolio"),
        "version": "1.0.0"
    })


@app.route("/metrics")
def metrics():
    logger.info("GET /metrics")
    return jsonify({
        "application": os.getenv("APP_NAME", "Flask DevOps Portfolio"),
        "status": "healthy",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "Development")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)