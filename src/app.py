from src.models.app_data import AppData
from src.models.session_handler import SessionHandler
from flask import Flask

app_server = Flask(__name__,
                   template_folder = "../templates",
                   static_folder="../static",
                   static_url_path=""
               )

app_data = AppData()
session_handler = SessionHandler()

from src.routes.dashboard import * 
from src.routes.internal_api import * 
from src.routes.external_api import * 
