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

    def load_app_data(self, path="persistent/app_data.pkl"):
        import os
        if os.path.exists(path):
            with open(path, "rb") as f:
                loaded_data = pickle.load(f)
                self.session_handler = loaded_data.session_handler
                self.data_source = loaded_data.data_source
                self.temp_data_source = loaded_data.temp_data_source
                self.models = loaded_data.models
                self.rec_requests = loaded_data.rec_requests
                self.system_status = loaded_data.system_status
                self.logger = loaded_data.logger
                self.default_model = loaded_data.default_model
                self.batch_size = loaded_data.batch_size
                self.auto_training = loaded_data.auto_training
                self.ui_theme = loaded_data.ui_theme

    def save_app_data(self, path="persistent/app_data.pkl"):
        import os
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)

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
