import json
import os

'''
Script below appends new users to the user.json database
'''

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

folder_path = 'JSON'
file_path_user = os.path.join(folder_path, 'user.json')

register_new_user('fp', 'sangilan', file_path_user)