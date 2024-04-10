import json
import os

'''
Script below appends new users to the user.json database
the id parameter will allow the program to connect the users to their corresponding
records while the username and password parameters will be used to authenticate the user to the program.
'''

folder_path = 'JSON'
file_path_user = os.path.join(folder_path, 'user.json')
file_path_acts = os.path.join(folder_path, 'activities.json')

def load_users(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

def save_users(file_path, users):
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)

def register_new_user(username, password, file_path):
    users = load_users(file_path)
    
    new_user_id = 1
    if users:
        new_user_id = max(user['id'] for user in users) + 1

    new_user = {
        'id': new_user_id,
        'username': username,
        'password': password
    }

    users.append(new_user)

    save_users(file_path, users)

#register_new_user('fp', 'sangilan', file_path_user)

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
    acts = load_activity(file_path)
    
    activity_found = False
    for activity in acts:
        if 'activity' in activity and activity['activity'] == activity_name:
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