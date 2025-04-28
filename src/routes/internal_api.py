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
        active_sessions = globals.APP_DATA.session_handler.get_count()
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
            "status_msg": e,
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
    return jsonify({
        "status": 200,
        "logs": [
            {
                "session_id": "a1b2-c3",
                "created": "2025-04-24T12:30:10Z",
                "last_seen": "2025-04-24T12:59:42Z",
                "preferences": ["coding", "technology"],
                "likes":   ["Q_03FWDBZG0", "ZLOhiGZZhVs", "zltBg1bUJjI"],
                "dislikes": ["ZvXoRoXm8DU"],
                "last_recs": [
                    {"id": "Q_03FWDBZG0", "score": 0.87},
                    {"id": "ZLOhiGZZhVs", "score": 0.85},
                    {"id": "zltBg1bUJjI", "score": 0.83},
                    {"id": "QM9j_qQZDnY", "score": 0.78},
                    {"id": "z7do1hhb6fE", "score": 0.76}
                ],
                "model_samples": 7,
                "last_trained": "2025-04-24T12:59:05Z"
            }
         ]
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
                "model_type": default_model,
                "batch_size": batch_size,
                "auto_training": auto_training,
                "ui_theme": ui_theme,
            }
        )
    except Exception as e:
        return jsonify( { "status": 500, "status_msg": e })


    


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

            path = "uploads/" + file.filename 
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
