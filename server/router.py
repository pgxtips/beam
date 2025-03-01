from flask import jsonify, send_from_directory
from .globals import app_server
import os

# API route
@app_server.route("/api/getRecommendations", methods=['get'])
def get_recommendations():
    return jsonify({"status": 200})

# serve React App
@app_server.route('/', defaults={'path': ''})
@app_server.route('/<path:path>')
def catch_all(path):
    # Make sure that all non-API routes serve index.html
    return app_server.send_static_file("index.html")

@app_server.errorhandler(404)
def reroute(_err):
    # Make sure that all non-API routes serve index.html
    return app_server.send_static_file("index.html")

