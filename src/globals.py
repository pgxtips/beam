from src.models.app_data import AppData
from flask import Flask

app_server = Flask(__name__,
                   template_folder = "../templates",
                   static_folder="../static",
                   static_url_path=""
               )

app_data = AppData()
