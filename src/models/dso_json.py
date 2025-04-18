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

    def get_attributes(self):
        conn = self.connect()
        if conn is None: 
            print("Connection Unavailable")
            return None 

        with conn: 
            data = json.load(conn) 
            flattened_data = self.flatten_data(data[0])
            return list(flattened_data.keys())

    def flatten_data(self, y):
        out = {}

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            else:
                out[name[:-1]] = x

        flatten(y)
        return out


