import flet as ft
import os
import Database
import json

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.authenticated = False

    def userVerification(self):
        folder_path = 'JSON'
        file_path_user = os.path.join(folder_path, 'user.json')
        try:
            with open(file_path_user, 'r') as file:
                user_data = json.load(file)
        except FileNotFoundError:
            print("Error: File 'user.json' not found")
            return False
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from 'users.json'")
            return False

        if self.username in user_data and user_data["password"] == self.password:
            self.authenticated = True
            return True
        else:
            return False
            
        
class Register:
    #register function
    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def registerUser(self, user_data):
        if self.username in user_data:
            return False
        else:
            user_data[self.username] = self.password
            with open('user.json', 'w') as file:
                json.dump(user_data, file)
            return True 
        
class Habit:
    
    def __init__(self, habit_name, habit_description, habit_days, habit_time):
        self.habit_name = habit_name
        self.habit_description = habit_description
        self.habit_days = habit_days
        self.habit_time = habit_time


class Calendar:
    def __init__(self, habit_name, habit_days, habit_time):
        self.habit_name = habit_name
        self.habit_days = habit_days
        self.habit_time = habit_time
        self.calendar = { "Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": [] }

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    

