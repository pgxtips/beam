from flask import jsonify, render_template, redirect
from src.globals import APP_SERVER

assert APP_SERVER

# dashboard routes
@APP_SERVER.route("/dashboard", methods=['get'])
def index():
    return render_template("index.html")

@APP_SERVER.route("/dashboard/datasource", methods=['get'])
def datasource():
    return render_template("datasource.html")

@APP_SERVER.route("/dashboard/sessions", methods=['get'])
def sessions():
    return render_template("sessions.html")

@APP_SERVER.route("/dashboard/monitor", methods=['get'])
def monitor():
    return render_template("monitor.html")

@APP_SERVER.route("/dashboard/metrics", methods=['get'])
def metrics():
    return render_template("metrics.html")

@APP_SERVER.route("/dashboard/logs", methods=['get'])
def logs():
    return render_template("logs.html")

@APP_SERVER.route("/dashboard/settings", methods=['get'])
def settings():
    return render_template("settings.html")


@APP_SERVER.errorhandler(404)
def page_not_found(e):
    return redirect('/dashboard')

# # serve React App
# @APP_SERVER.route('/', defaults={'path': ''})
# @APP_SERVER.route('/<path:path>')
# def catch_all(path):
#     # Make sure that all non-API routes serve index.html
#     return APP_SERVER.send_static_file("index.html")
#
# @APP_SERVER.errorhandler(404)
# def reroute(_err):
#     # Make sure that all non-API routes serve index.html
#     return APP_SERVER.send_static_file("index.html")
#
