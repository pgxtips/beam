from src.models.app_data import AppData
import src.globals as globals 
from flask import Flask

globals.APP_SERVER = Flask(__name__,
                   template_folder = "../templates",
                   static_folder="../static",
                   static_url_path=""
               )

globals.APP_DATA = AppData()

from src.routes.dashboard import * 
from src.routes.internal_api import * 
from src.routes.external_api import * 
