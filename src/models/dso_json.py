from .dso_abc import DSO
from src.utils import flatten_dict

from itertools import chain  
import json

class DSJsonFileObject(DSO):
    def __init__(self, src):
        super().__init__(src)

    def connect(self):
        try:
            return open(self.src, "r")
        except Exception as e:
            print("Error connecting:", e)
            return None

    def load_data(self):
        conn = self.connect()
        if conn is None: 
            print("Connection Unavailable")
            return None 

        data = []
        keys = set()

        def add_keys(arr):
            for el in arr:
                keys.add(el)

        with conn: 
            d = json.load(conn) 
            for el in d:
                flattened_data = flatten_dict(el)
                data.append(flattened_data)
                add_keys(flattened_data.keys())

        self.data = data
        self.keys = list(keys)

    def load_tags(self):
        if not self.tag_column:
            print("Error: no tag column set")
            return

        if not self.data:
            print("Error: no tag column set")
            return

        tag_data = self.get_col_data(self.tag_column)

        if not tag_data:
            print("Error: no data in specified tag column")
            return

        filtered_data = (tags for tags in tag_data if tags is not None)
        flattened_data = list(chain(*filtered_data))
        tag_set = set(flattened_data)

        self.tags = list(tag_set)

    def get_data(self):
        if not self.data: 
            print("No Data Available")
            return None 

        return self.data 

    def get_col_data(self, col_name: str):
        if not self.data: 
            print("No Data Available")
            return None 

        out = [ el.get(col_name) for el in self.data ]
        return out

    def get_keys(self):
        if not self.keys: 
            print("No Data Available")
            return None 

        return self.keys 

    def get_tags(self):
        if not self.tag_column: 
            print("No Tag Column Set")
            return None 

        if not self.data: 
            print("No Data Available")
            return None 

        if not self.tags:
            self.load_tags()

        return self.tags
