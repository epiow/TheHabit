import json
import os

import DataIO
import pandas as pd
import numpy as np
from datetime import datetime

class Database:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.io = DataIO.DataIO(self.file_path)

    def __init__(self, io: DataIO.DataIO):
        self.io = io
           
    def create_user(self, username, password):
        data = self.io.load_data()
        for user in data:
            if user["username"] == username:
                return False
            
        new_user = {
            'username': username,
            'password': password,
            'activities': []
        }
        data.append(new_user)
        self.io.save_data(data=data)
        
    def create_activity(self, user_id, activity_name, time_set, time_elapsed):
        data = self.io.load_data()
        today_date = datetime.today().strftime('%Y/%m/%d')
        user_found = False
        for user in data:
            if user_id == user["username"]:
                user_found = True
                activity_found = False
                for activity in user["activities"]:
                    if activity_name in activity["name"]:
                        activity_found = True
                        for entry in activity["times_performed"]:
                            if entry["date_performed"] == today_date:
                                entry["count"] += 1
                                entry["time_elapsed"]
                                break
                        else:
                            new_activity_entry = {
                                "date_performed": today_date,
                                "time_set": time_set,
                                "time_elapsed": time_elapsed,
                                "count": 1 
                            }
                            activity["times_performed"].append(new_activity_entry)
                        break
                if not activity_found:
                    new_activity = {
                        "name": activity_name,
                        "times_performed": [
                            {
                                "date_performed": today_date,
                                "time_set": time_set,
                                "time_elapsed": time_elapsed,
                                "count": 1  
                            }
                        ]
                    }
                    user["activities"].append(new_activity)
                    break
        self.io.save_data(data)