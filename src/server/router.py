from flask import jsonify, render_template
from src.globals import app_server

# API routes
# TODO: change method to post
@app_server.route("/api/getRecommendations", methods=['get'])
def get_recommendations():
    return jsonify({"status": 200})

# dashboard routes
@app_server.route("/dashboard", methods=['get'])
def index():
    return render_template("index.html")

@app_server.route("/dashboard/datasource", methods=['get'])
def datasource():
    return render_template("datasource.html")

@app_server.route("/dashboard/sessions", methods=['get'])
def sessions():
    return render_template("sessions.html")

@app_server.route("/dashboard/monitor", methods=['get'])
def monitor():
    return render_template("monitor.html")

@app_server.route("/dashboard/logs", methods=['get'])
def logs():
    return render_template("logs.html")

@app_server.route("/dashboard/settings", methods=['get'])
def settings():
    return render_template("settings.html")


# # serve React App
# @app_server.route('/', defaults={'path': ''})
# @app_server.route('/<path:path>')
# def catch_all(path):
#     # Make sure that all non-API routes serve index.html
#     return app_server.send_static_file("index.html")
#
# @app_server.errorhandler(404)
# def reroute(_err):
#     # Make sure that all non-API routes serve index.html
#     return app_server.send_static_file("index.html")
#
