from .dso_abc import DSO

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
        attributes = set()

        def add_attributes(arr):
            for el in arr:
                attributes.add(el)

        with conn: 
            d = json.load(conn) 
            for el in d:
                flattened_data = flatten_data(el)
                data.append(flattened_data)
                add_attributes(flattened_data.keys())

        self.data = data
        self.attributes = list(attributes)

    def get_data(self, selected_attributes):
        if not self.data: 
            print("No Data Available")
            return None 

        out = [
           {attr: el.get(attr) for attr in selected_attributes} 
           for el in self.data
        ]

        return out

    def get_attributes(self):
        if not self.attributes: 
            print("No Data Available")
            return None 

        return self.attributes 


def flatten_data(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out
