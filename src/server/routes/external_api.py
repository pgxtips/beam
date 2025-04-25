from flask import jsonify, render_template
from src.globals import app_server

# External API routes 
@app_server.route("/extern/getRecommendations", methods=['get'])
def get_recommendations():
    return jsonify({"status": 200})
