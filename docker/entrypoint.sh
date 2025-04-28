#!/bin/sh
set -e

nginx &
uv run gunicorn -b 0.0.0.0:6969 src.app:APP_SERVER
