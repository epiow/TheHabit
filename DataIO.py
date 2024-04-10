import json
import os
class DataIO:
    def __init__(self, file_path):
        self.file_path = file_path
    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []
    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
