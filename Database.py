import json
import os
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

        new_user = {
            'username': username,
            'password': password,
            'activities': []
        }
        data.append(new_user)
        self.save_data(data=data)

    def create_activity(self, user_id, activity_name, time_set, time_elapsed):
        print(self.file_path)
        data = self.load_data()
        user_found = False
        for user in data:
            if(user_id == user["username"]):
                print("user found")
                user_found = True
                activity_found = False
                for activity in user["activities"]:
                    print(activity)
                    if(activity_name in activity["name"]):
                        print("activity found")
                        activity_found = True
                        new_activity_entry = {
                            "date_performed": datetime.today().strftime('%Y/%m/%d'),
                            "time_set": time_set,
                            "time_elapsed": time_elapsed
                        }
                        activity["times_performed"].append(new_activity_entry)
                        break
                if(activity_found == False):
                    print("activity not found")
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
        self.save_data(data)
        
            

                    

                    


'''
The following script is used to create/update the users' activity log in the activity chart
'''
def load_activity(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

def save_activities(file_path, activities):
    with open(file_path, 'w') as file:
        json.dump(activities, file, indent=4)

def create_activity(self, user_id, activity_name, time_duration, time_elapsed):
    data = load_activity(self.file_path)
    
    activity_found = False
    for i in data:

        if 'activitt' in activity and activity['activity'] == activity_name:
            for day_date in performed:
                if day_date not in activity['done']:
                    activity['done'].append(day_date)
            activity_found = True
            break

    if not activity_found:
        new_activity = {
            'user_id': user_id,
            'activity': activity_name,
            'activity_kind': timed,
            'done': performed
        }
        acts.append(new_activity)

    save_activities(file_path, acts)

