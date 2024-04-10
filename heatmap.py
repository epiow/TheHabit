import json
import os
from datetime import datetime
class Insights:
    file_path = os.path.join('JSON', 'data.json')
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
    
    def heatmap(self, user_id):
        data = json.load(self.file_path)
        for user in data:
            if(user_id == user["username"]):
                date = 0
                for activity in user["activities"]:
                    if(activity["date_performed"] == 0) # TO-DO