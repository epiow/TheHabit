import flet as ft
import os
import Database
import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def setHabits(self):
        folder_path = 'JSON'
        file_path_acts = os.path.join(folder_path, 'activities.json')
        with open(file_path_acts, 'r') as acts:
            activities = json.load(acts)
        
            for activity in activities:
                if self.userID == int(activity['user_id']):
                    habit = Habit(activity['activity'], activity['activity_kind'], activity["done"])   
                    print(self.username + ' ' + habit.habit_name)
class Login(User):
    def __init__(self, username, password):
        super().__init__(username, password)

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

        for users in user_data:
            if self.username == users['username'] and self.password == users['password']:
                self.userID = users['id']
                super().setHabits()
                return True
        #if self.username in user_data and user_data["password"] == self.password:
        #    self.authenticated = True
        #    return True
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
        
class Habit(User):
    def __init__(self, habit_name, habit_description, habit_setting):
        self.habit_name = habit_name
        self.habit_description = habit_description
        self.habit_TimeSetter(habit_setting)

    def habit_TimeSetter(self, habit_setting):
        for x in habit_setting:
            dayOfActivity = Calendar(x[0], x[1])
class Calendar(Habit):
    def __init__(self, habit_date, habit_day):
        #self.specific_habit = habit_name
        self.habit_date = habit_date
        self.habit_day = habit_day
        self.calendar = { "Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": [] }


login = Login("fp", "sangilan")
login.userVerification()
