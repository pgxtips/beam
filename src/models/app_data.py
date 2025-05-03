import uuid
import pickle 
from typing import Optional

from src.recommender.abc_recommender import Recommender
from src.recommender.data_processing import prepare_data
from src.recommender.logistic_recommender import LogisticRecommender
from src.recommender.none_recommender import NoneRecommender 

from src.models.session_data import SessionData
from src.models.session_handler import SessionHandler
from src.models.logger import Logger

class AppData:
    def __init__(self):
        self.__session_handler = SessionHandler() 
        self.data_source = None

        self.temp_data_source = None

        self.__models: dict[str, Optional[Recommender]] = {
            "logistic": None,
            "none": None
        }

        self.rec_requests = 0

        self.system_status = "Inoperative"
        self.logger = Logger()
        self.default_model = "logistic"
        # ACE ?? 
        self.batch_size = 5
        self.auto_training = True
        self.ui_theme = "light"

    def load_app_data(self, path="persistent/app_data.pkl"):
        try:
            import os
            if os.path.exists(path):
                with open(path, "rb") as f:
                    loaded_data = pickle.load(f)
                    self.__session_handler = loaded_data.__session_handler
                    self.data_source = loaded_data.data_source
                    self.temp_data_source = loaded_data.temp_data_source
                    self.__models = loaded_data.__models
                    self.rec_requests = loaded_data.rec_requests
                    self.system_status = loaded_data.system_status
                    self.logger = loaded_data.logger
                    self.default_model = loaded_data.default_model
                    self.batch_size = loaded_data.batch_size
                    self.auto_training = loaded_data.auto_training
                    self.ui_theme = loaded_data.ui_theme
        except Exception as e:
            print("error: Failed to load from pickle")

    def save_app_data(self, path="persistent/app_data.pkl"):
        import os
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)

        with open(path, "wb") as f:
            pickle.dump(self, f)

    def get_system_status(self):
        if not self.data_source:
            return "No Data Source"
        else:
            return "Operational"

    def get_session_handler(self):
        return self.__session_handler

    def get_default_model(self):
        return self.default_model

    def get_model(self, session_model_str):
        if not session_model_str in self.__models.keys():
            raise Exception(f"No recommender created for the '{session_model_str}' model")

        if not self.__models.get(session_model_str):
            self.build_models()

        return self.__models.get(session_model_str)


    def build_models(self):
        if not self.data_source:
            raise Exception("There is not a valid datasource")

        # build logistic recommender
        ids, vectoriser, X = prepare_data(self.data_source)
        logistic_recommender = LogisticRecommender(X, ids, vectoriser) 
        self.__models["logistic"] = logistic_recommender

        # build none recommender
        logistic_recommender = NoneRecommender(ids) 
        self.__models["none"] = logistic_recommender

    def set_session_handler(self, session_handler):
        self.session_handler = session_handler
        self.save_app_data()

    def set_temp_datasource(self, dso):
        self.temp_data_source = dso
        self.save_app_data()

    def set_datasource(self, dso):
        self.data_source = dso
        self.save_app_data()
