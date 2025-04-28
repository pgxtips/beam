from flask import jsonify, render_template
from src.globals import APP_SERVER

# External API routes 
@APP_SERVER.route("/extern/getRecommendations", methods=['get'])
def get_recommendations():
    return jsonify({"status": 200})
