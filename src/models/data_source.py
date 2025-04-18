from .dso_abc import DSO
from .dso_json import DSJsonFileObject
from .dso_database import DSDatabaseObject

class DataSource:
    def __init__(self, type, src):
        self.dso = self.create_dso(type, src)
        self.target_feature_idx = -1
        return

    def create_dso(self, dso_type, src) -> DSO:
        strategies = {
            "database": DSDatabaseObject,
            "file": DSJsonFileObject
        }
        if dso_type not in strategies:
            raise ValueError("Invalid data source type")
        return strategies[dso_type](src)

    def get_features(self):
        return self.dso.get_attributes()

    def get_data(self):
        pass
        # return {
        #     "features": self.ds_features + self.metric_features,
        #     "target_feature": self.ds_features[self.target_feature_idx]
        # }
