from flask import Flask
from .globals import app_server
from .router import * 

if __name__ == "__main__":
    app_server.run(host="0.0.0.0", port=6969, debug=True)
