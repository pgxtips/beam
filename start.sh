# !/bin/bash
uv run gunicorn -b 0.0.0.0:6969 src.app:app_server
