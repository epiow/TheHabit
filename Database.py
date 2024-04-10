import json
import os
import DataIO
from datetime import datetime
'''
Script below appends new users to the user.json database
the id parameter will allow the program to connect the users to their corresponding
records while the username and password parameters will be used to authenticate the user to the program.
'''
class Database:
    file_path = os.path.join('JSON', 'data.json')
    def __init__(self, file_path):
        self.file_path = file_path
        self.io = DataIO.DataIO(self.file_path)
        
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
        self.io.save_data(data=data)
        return False

    def create_activity(self, user_id, activity_name, time_set, time_elapsed):
        data = self.io.load_data()
        user_found = False
        for user in data:
            if(user_id == user["username"]):
                user_found = True
                activity_found = False
                for activity in user["activities"]:
                    if(activity_name in activity["name"]):
                        activity_found = True
                        new_activity_entry = {
                            "date_performed": datetime.today().strftime('%Y/%m/%d'),
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
                                "date_performed": datetime.today().strftime('%Y/%m/%d'),
                                "time_set": time_set,
                                "time_elapsed": time_elapsed
                            }
                        ]
                    }
                    user["activities"].append(new_activity)
                    break
        self.io.save_data(data)