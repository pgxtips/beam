import uuid
import pickle 
from typing import Optional

from src.models.session_data import SessionData
from src.models.session_handler import SessionHandler
from src.models.logger import Logger 

class AppData:
    def __init__(self):
        self.session_handler = SessionHandler() 
        self.data_source = None

        self.temp_data_source = None

        self.models = {
            "logistic": None,
            "similarity": None
        }

        self.rec_requests = 0

        self.system_status = "Incomplete"
        self.logger = Logger()
        self.default_model = "logistic"
        self.batch_size = 5
        self.auto_training = True
        self.ui_theme = "light"

    @staticmethod
    def load_app_data(path="app_data.pkl"):
        import os
        if os.path.exists("app_data.pkl"):
            with open(path, "rb") as f:
                return pickle.load(f)

    def save_app_data(self, path="app_data.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self, f)

    def get_system_status(self):
        return "Operational"

    def get_session_handler(self):
        return self.session_handler

    def get_default_model(self):
        return self.default_model

    def set_session_handler(self, session_handler):
        self.session_handler = session_handler
        self.save_app_data()

    def set_temp_datasource(self, dso):
        self.temp_data_source = dso
        self.save_app_data()

    def set_datasource(self, dso):
        self.data_source = dso
        self.save_app_data()
