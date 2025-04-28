from .dso_abc import DSO
from .dso_json import DSJsonFileObject
from .dso_database import DSDatabaseObject

class DataSource:
    def __init__(self, dso_type, src):

        if dso := create_dso(dso_type, src):
            self.dso_type = dso_type
            dso.load_data()

            if dso_type == "demo":
                dso.set_content_id_column("id")
                dso.set_tag_column("snippet_tags")

        self.dso = dso

    def set_tag_column(self, col_name: str):
        self.dso.set_tag_column(col_name)

    def set_content_id_column(self, col_name: str):
        self.dso.set_content_id_column(col_name)

    def get_keys(self):
        return self.dso.get_keys()

    def get_tags(self):
        return self.dso.get_tags()

    def get_col_data(self, col_name: str):
        return self.dso.get_col_data(col_name)

    def get_type(self):
        return self.dso_type

    def get_data(self):
        return self.dso.get_data()

    def get_src(self):
        return self.dso.get_src()

    def get_content_id_column(self):
        return self.dso.get_content_id_column()

    def get_tag_column(self):
        return self.dso.get_tag_column()

def create_dso(dso_type, src) -> DSO:
    strategies = {
        "database": DSDatabaseObject,
        "file": DSJsonFileObject,
        "demo": DSJsonFileObject
    }
    if dso_type not in strategies:
        raise Exception("Invalid data source type")

    if dso_type == "demo":
        return strategies["demo"]("./data/youtube_data.json")

    return strategies[dso_type](src)
