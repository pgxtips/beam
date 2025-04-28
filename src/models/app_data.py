import uuid
from typing import Optional

from src.models.session_data import SessionData
from src.models.session_handler import SessionHandler

class AppData:
    def __init__(self):
        self.session_handler = SessionHandler() 
        self.data_source = None
        self.models = {
            "logistic": None,
            "similarity": None
        }

        self.default_model = "logistic"

    def load_conf(self):
        pass

    def get_session_handler(self):
        return self.session_handler

    def get_default_model(self):
        return self.default_model

    def set_session_handler(self, session_handler):
        self.session_handler = session_handler

