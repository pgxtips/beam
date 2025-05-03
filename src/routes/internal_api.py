from enum import auto
from flask import jsonify, request

from src.globals import APP_SERVER 
from src.models import data_source
from src.utils import *

# Internal API routes 
@APP_SERVER.route("/internal/get/index", methods=['get'])
def get_index_data():
    import src.globals as globals

    try:
        rec_requests = globals.APP_DATA.rec_requests
        active_sessions = globals.APP_DATA.get_session_handler().get_count()
        system_status = globals.APP_DATA.get_system_status()

        return jsonify({
            "status": 200,
            "rec_requests": rec_requests,
            "active_sessions": active_sessions,
            "system_status": system_status,
        })

    except Exception as e:
        return jsonify({
            "status": 500,
            "status_msg": str(e),
            "rec_requests": "43",
            "active_sessions": "2",
            "system_status": "Operational",
        })


@APP_SERVER.route("/internal/get/datasource", methods=['get'])
def get_datasource_data():
    import src.globals as globals

    dso = globals.APP_DATA.data_source

    if not dso:
        return jsonify({
            "status": 200,
            "message": "no data source available"
        })

    source_type = globals.APP_DATA.data_source.get_type()

    source_data = globals.APP_DATA.data_source.get_src().split("/")
    source_data = source_data[len(source_data)-1]

    attributes = globals.APP_DATA.data_source.get_keys()

    content_column = globals.APP_DATA.data_source.get_content_id_column()
    tag_column = globals.APP_DATA.data_source.get_tag_column()

    return jsonify(
        {
            "status": 200,
            "source_type": source_type,
            "source_data": source_data,
            "attributes": attributes,
            "content_column": content_column,
            "tag_column": tag_column,
        }
    )

@APP_SERVER.route("/internal/get/sessions", methods=['get'])
def get_session_data():
    try:
        import src.globals as globals

        session_handler = globals.APP_DATA.get_session_handler()
        assert session_handler

        session_data = session_handler.get_sessions() or {}

        return jsonify({
            "status": 200,
            "session_data": [
                {
                    "session_id": key,
                    "created": val.get_created() or "N/A",
                    "last_seen": val.get_last_seen() or "N/A",
                    "preferences": [x for x in val.get_preferences()] or [],
                    "likes":   [x for x in val.get_all_likes()] or [],
                    "dislikes": [x for x in val.get_all_dislikes()] or [],
                    "last_trained": val.get_last_train() or "N/A",
                    "active_model": val.get_model() or "N/A",
                    "history": [x for x in val.get_history()] or [],
                } 
                for key, val in session_data.items()
             ]
        })
    except Exception as e:
        return jsonify({
            "status": 500,
            "status_msg": str(e)
        })

@APP_SERVER.route("/internal/get/monitor", methods=['get'])
def get_monitor_data():
    cpu_usage_data = get_cpu_usage()
    memory_usage_data = get_memory_usage()
    net_in, net_out = get_network_usage()

    return jsonify(
        {
            "status": 200,
            "cpu_usage": cpu_usage_data,
            "memory_usage": memory_usage_data,
            "net_in": net_in,
            "net_out": net_out,
        }
    )

@APP_SERVER.route("/internal/get/logs", methods=['get'])
def get_log_data():
    return jsonify({
        "status": 200,
        "logs": [
            {
                "timestamp": "2025-04-25T10:15:00Z",
                "type": "recommendation_sent",
                "session_id": "sesh-001",
                "message": "Sent 5 recommendations",
                "details": {
                    "model": "logistic",
                    "content_ids": ["vid01", "vid02", "vid03", "vid04", "vid05"]
                }
            }
        ]
    })

@APP_SERVER.route("/internal/get/settings", methods=['get'])
def get_settings_data():
    try:
        import src.globals as globals

        default_model = globals.APP_DATA.default_model
        batch_size = globals.APP_DATA.batch_size
        auto_training = globals.APP_DATA.auto_training
        ui_theme = globals.APP_DATA.ui_theme

        return jsonify(
            {
                "status": 200,
                "default_model": default_model,
                "batch_size": batch_size,
                "auto_training": auto_training,
                "ui_theme": ui_theme,
            }
        )
    except Exception as e:
        return jsonify( { "status": 500, "status_msg": str(e) })

@APP_SERVER.route("/internal/get/deletepkl", methods=['get'])
def get_delete_pkl():
    try:
        import os
        path="persistent/app_data.pkl"
        if os.path.exists(path):
            os.remove(path)

        return jsonify( { "status": 200, } )
    except Exception as e:
        return jsonify( { "status": 500, "status_msg": str(e) })


# --------------------------
#       POST Requests
# --------------------------
@APP_SERVER.route("/internal/post/datasource", methods=['post'])
def post_datasource_data():
    from src.models.data_source import DataSource
    import src.globals as globals

    try: 
        formData = request.form
        source_type = formData["sourceType"]
        file_upload = formData.get("file_upload")

        if source_type == "demo":
            dso = DataSource("demo", "")
            globals.APP_DATA.set_datasource(dso)

            return jsonify( { "status": 200 })

        if (file_upload):
            file = request.files.get("fileInput")
            save_file(file)

            path = "persistent/uploads/" + file.filename 
            data_source = DataSource("file", path)
            keys = data_source.get_keys()

            globals.APP_DATA.set_temp_datasource(data_source)

            return jsonify({ "status": 200, "keys": keys })

        else:
            temp_ds = globals.APP_DATA.temp_data_source
            if not temp_ds:
                globals.APP_DATA.set_temp_datasource(globals.APP_DATA.data_source)

            assert temp_ds

            content_column = formData["contentColumn"]
            tag_column = formData["tagColumn"]

            temp_ds.set_content_id_column(content_column)
            temp_ds.set_tag_column(tag_column)

            globals.APP_DATA.set_datasource(temp_ds)

        return jsonify( { "status": 200 })

    except Exception as e:
        return jsonify( { "status": 500, "error": e })


@APP_SERVER.route("/internal/post/settings", methods=['post'])
def post_settings_data():
    try: 
        from src.models.data_source import DataSource
        import src.globals as globals

        formData = request.form
        default_model = formData["default_model"] 
        batch_size = formData["batch_size"] 
        auto_training = formData["auto_training"] 
        ui_theme = formData["ui_theme"] 

        auto_training = auto_training == "true"

        globals.APP_DATA.default_model = default_model
        globals.APP_DATA.batch_size = batch_size
        globals.APP_DATA.auto_training = bool(auto_training)
        globals.APP_DATA.ui_theme = ui_theme
 
        globals.APP_DATA.save_app_data()
        return jsonify({ 
            "status": 200,
            "default_model": default_model,
            "batch_size": batch_size,
            "auto_training": auto_training,
            "ui_theme": ui_theme,
        })

    except Exception as e:
        return jsonify( { "status": 500, "error": e })
