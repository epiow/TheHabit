import json
import os
from datetime import datetime
'''
Script below appends new users to the user.json database
the id parameter will allow the program to connect the users to their corresponding
records while the username and password parameters will be used to authenticate the user to the program.
'''
class Database:
    def __init__(self):
        self.file_path = './JSON/user.json'

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def register_user(self, username, password):
        data = self.load_data()
        for user in data:
            if user["username"] == username:
                print("duplicate found")
                return
        new_user = {
            'username': username,
            'password': password,
            'activities': []
        }
        data.append(new_user)
        self.save_data(data=data)

    def create_activity(self, user_id, activity_name, time_set, time_elapsed):
        data = self.load_data()
        user_found = False
        for user in data:
            if(user_id == user["username"]):
                user_found = True
                activity_found = False
                for activity in user["activities"]:
                    if(activity_name in activity["name"]):
                        activity_found = True
                        new_activity_entry = {
                            "date_performed": datetime.today().timestamp(),
                            "time_set": time_set,
                            "time_elapsed": time_elapsed
                        }
                        activity["times_performed"].append(new_activity_entry)
                        break
                if(activity_found == False):
                    new_activity = {
                        "name": activity_name,
                        "times_performed": [
                            {
                                "date_performed": datetime.today().timestamp(),
                                "time_set": time_set,
                                "time_elapsed": time_elapsed
                            }
                        ]
                    }
                    user["activities"].append(new_activity)
                    break
        self.save_data(data)
