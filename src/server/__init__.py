from src.globals import app_server
from .routes.dashboard import * 
from .routes.internal_api import * 
from .routes.external_api import * 

def start_server():
    app_server.run(host="0.0.0.0", port=6969, debug=True)
