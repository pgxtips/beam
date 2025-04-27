from flask import jsonify
from src.app import app_server
from src.utils import *

# Internal API routes 
@app_server.route("/internal/index", methods=['get'])
def get_index_data():
    return jsonify(
        {
            "rec_requests": "43",
            "active_sessions": "2",
            "system_status": "Operational",
        }
    )

@app_server.route("/internal/datasource", methods=['get'])
def get_datasource_data():
    return jsonify(
        {
            "source_type": "1",
            "source_data": "youtube_json.json",
            "attributes": ["id", "content", "last_seen", "created_at"],
            "content_column": "0",
            "tag_column": "1",
        }
    )

@app_server.route("/internal/sessions", methods=['get'])
def get_session_data():
    return jsonify([
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
        },
        {
            "session_id": "f4e5-d6",
            "created": "2025-04-24T12:42:03Z",
            "last_seen": "2025-04-24T12:58:11Z",
            "preferences": ["gaming"],
            "likes":   [],
            "dislikes": [],
            "last_recs": [
                {"id": "xA1BCdEFgh0", "score": 0.65},
                {"id": "7TuvWxyz123", "score": 0.63},
                {"id": "mNOPqr45STU", "score": 0.61}
                ],
            "model_samples": 2,
            "last_trained": "2025-04-24T12:42:04Z"
        },
        {
            "session_id": "8a9b-00",
            "created": "2025-04-24T11:55:44Z",
            "last_seen": "2025-04-24T12:57:22Z",
            "preferences": ["music", "lofi", "study"],
            "likes":   ["LOFIbeat001", "LOFIbeat007", "CalmTrack22"],
            "dislikes": ["HeavyMetal99", "Dubstep77"],
            "last_recs": [
                {"id": "LOFIbeat014", "score": 0.91},
                {"id": "CalmTrack25", "score": 0.88},
                {"id": "StudySound10", "score": 0.86},
                {"id": "RelaxLoop03", "score": 0.85}
                ],
            "model_samples": 12,
            "last_trained": "2025-04-24T12:56:58Z"
        }
    ])

@app_server.route("/internal/monitor", methods=['get'])
def get_monitor_data():
    cpu_usage_data = get_cpu_usage()
    memory_usage_data = get_memory_usage()
    net_in, net_out = get_network_usage()

    return jsonify(
        {
            "cpu_usage": cpu_usage_data,
            "memory_usage": memory_usage_data,
            "net_in": net_in,
            "net_out": net_out,
        }
    )

@app_server.route("/internal/logs", methods=['get'])
def get_log_data():
    return jsonify([
        {
            "timestamp": "2025-04-25T10:15:00Z",
            "type": "recommendation_sent",
            "session_id": "sesh-001",
            "message": "Sent 5 recommendations",
            "details": {
                "model": "logistic",
                "content_ids": ["vid01", "vid02", "vid03", "vid04", "vid05"]
            }
        },
        {
            "timestamp": "2025-04-25T10:16:45Z",
            "type": "preference_updated",
            "session_id": "sesh-002",
            "message": "User added 3 new preferences",
            "details": {
                "added": ["music", "comedy", "technology"],
                "removed": []
            }
        },
        {
            "timestamp": "2025-04-25T10:18:30Z",
            "type": "like_event",
            "session_id": "sesh-001",
            "message": "User liked a content item",
            "details": {
                "content_id": "vid07"
            }
        },
        {
            "timestamp": "2025-04-25T10:20:05Z",
            "type": "dislike_event",
            "session_id": "sesh-003",
            "message": "User disliked a content item",
            "details": {
                "content_id": "vid11"
            }
        },
        {
            "timestamp": "2025-04-25T10:22:10Z",
            "type": "model_trained",
            "session_id": "sesh-001",
            "message": "Retrained logistic model with 87 samples",
            "details": {
                "model": "logistic",
                "samples": 87,
                "accuracy": "0.83"
            }
        },
        {
            "timestamp": "2025-04-25T10:25:00Z",
            "type": "recommendation_sent",
            "session_id": "sesh-004",
            "message": "Sent 3 recommendations",
            "details": {
                "model": "similarity",
                "content_ids": ["vid21", "vid22", "vid23"]
            }
        }
    ])

@app_server.route("/internal/settings", methods=['get'])
def get_settings_data():
    return jsonify(
        {
            "model_type": "1",
            "batch_size": "5",
            "auto_training": "1",
            "training_interval": "5",
            "ui_theme": "1",
        }
    )
