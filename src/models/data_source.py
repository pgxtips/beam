from .dso_abc import DSO
from .dso_json import DSJsonFileObject
from .dso_database import DSDatabaseObject

class DataSource:
    def __init__(self, type, src):
        dso = self.create_dso(type, src)
        if dso:
            dso.load_data()

        self.dso = dso
        self.selected_features = []
        self.target_feature_idx = -1

    def create_dso(self, dso_type, src) -> DSO:
        strategies = {
            "database": DSDatabaseObject,
            "file": DSJsonFileObject
        }
        if dso_type not in strategies:
            raise Exception("Invalid data source type")
        return strategies[dso_type](src)

    def get_all_features(self):
        return self.dso.get_attributes()

    def set_selected(self, selected):
        self.selected_features = selected

    def get_data(self):
        return self.dso.get_data(self.selected_features)
