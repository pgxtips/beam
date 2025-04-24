from src.globals import app_server
from .router import * 

def start_server():
    app_server.run(host="0.0.0.0", port=6969, debug=True)
