from flask import jsonify, render_template, request
from src.globals import APP_SERVER

import traceback 

# External API routes 

@APP_SERVER.route("/external/createSession", methods=['get'])
def create_session():
    try:
        import src.globals as globals
        session_handler = globals.APP_DATA.get_session_handler()
        assert session_handler

        session_id = session_handler.create_new()

        globals.APP_DATA.save_app_data()

        return jsonify({
            "status": 200,
            "session_id": session_id
        })
    except Exception as e:
        return jsonify({
            "status": 500,
            "status_msg": str(e)
        })

@APP_SERVER.route("/external/like", methods=['post'])
def like_content():
    try: 
        import src.globals as globals

        formData = request.form
        session_id = formData["session_id"]
        content_id = formData["content_id"]

        session_handler = globals.APP_DATA.get_session_handler()
        session_data = session_handler.get_session_data(session_id)
        if not session_data:
            raise Exception(f"No session exists for: {session_id}")

        session_data.add_like(content_id)

        return jsonify({ "status": 200 })
    except Exception as e:
        return jsonify({ "status": 500, "status_msg": str(e)})

@APP_SERVER.route("/external/dislike", methods=['post'])
def dislike_content():
    try: 
        import src.globals as globals

        formData = request.form
        print(formData)
        session_id = formData["session_id"]
        content_id = formData["content_id"]

        session_handler = globals.APP_DATA.get_session_handler()
        session_data = session_handler.get_session_data(session_id)
        if not session_data:
            raise Exception(f"No session exists for: {session_id}")

        session_data.add_dislike(content_id)

        return jsonify({ "status": 200 })
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        return jsonify({ "status": 500, "status_msg": str(e)})

@APP_SERVER.route("/external/recommend", methods=['post'])
def get_recommendations():
    try:
        import src.globals as globals

        formData = request.form
        session_id = formData["session_id"]

        app_data = globals.APP_DATA
        if not app_data:
            raise Exception("App data is not initialized.")

        session_handler = app_data.get_session_handler()
        session_data = session_handler.get_session_data(session_id)
        if not session_data:
            raise Exception(f"No session exists for: {session_id}")

        session_model_str = session_data.get_model()
        recommender = app_data.get_model(session_model_str)
        if not recommender:
            raise Exception(f"No recommender created for the '{session_model_str}' model")

        rec = recommender.recommend(session_id, 5)

        return jsonify({"status": 200, "recommendations": rec})

    except Exception as e:
        print("error:", e)
        return jsonify({"status": 500, "status_msg": str(e)})
