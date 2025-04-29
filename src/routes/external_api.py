from flask import jsonify, render_template, request
from src.globals import APP_SERVER

# External API routes 

@APP_SERVER.route("/external/createSession", methods=['get'])
def create_session():
    try:
        session_id = "5a1e185f-8cd4-4f42-8e28-0679a5718b7d"

        return jsonify({
            "status": 200,
            "session_id": session_id
        })
    except Exception as e:
        return jsonify({
            "status": 500,
            "status_msg": e
        })

@APP_SERVER.route("/external/like", methods=['post'])
def like_content():
    try: 
        formData = request.form
        print(formData)
        session_id = formData["session_id"]
        content_id = formData["content_id"]

        # TODO: perform action ...

        return jsonify({ "status": 200 })
    except Exception as e:
        return jsonify({ "status": 500, "status_msg": e})

@APP_SERVER.route("/external/dislike", methods=['post'])
def dislike_content():
    try: 
        formData = request.form
        print(formData)
        session_id = formData["session_id"]
        content_id = formData["content_id"]

        # TODO: perform action ...

        return jsonify({ "status": 200 })
    except Exception as e:
        return jsonify({ "status": 500, "status_msg": e})

@APP_SERVER.route("/external/getRecommendations", methods=['get'])
def get_recommendations():
    return jsonify({"status": 200})
