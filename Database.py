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

    def load_data():
        if os.path.exists(file_path):
            with(file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_data(data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def register_user(username, password):
        users = load_users(file_path)
        
        new_user_id = 1
        if users:
            new_user_id = max(user['id'] for user in users) + 1

        new_user = {
            'id': new_user_id,
            'username': username,
            'password': password,
            'activities': []
        }
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

def create_activity(user_id, activity_name, timed, performed, file_path):
    data = load_activity(file_path)
    
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

#create_activity('1', 'jogging', 'no', [[1, 'tuesday']], file_path_acts)