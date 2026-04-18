"""
Health-Check Monitoring Service
Exposes /health and /status endpoints for infrastructure liveness probes.
"""

from flask import Flask, jsonify
from datetime import datetime, timezone
import platform
import os

app = Flask(__name__)

SERVICE_NAME = os.getenv("SERVICE_NAME", "health-monitor")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "1.0.0")


@app.route("/health")
def health():
    """Lightweight liveness probe — returns 200 if the process is alive."""
    return jsonify({"status": "healthy"}), 200


@app.route("/status")
def status():
    """Rich readiness probe — returns runtime metadata for diagnostics."""
    return jsonify({
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "hostname": platform.node(),
        "python_version": platform.python_version(),
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
