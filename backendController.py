import flet as ft
import os
import DataIO
import Database
import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.io = DataIO.DataIO('./JSON/data.json')
    def setHabits(self):
        data = self.io.load_data()
        for user in data:
            if(self.username == user["username"]):
                for activity in user["activities"]:
                    habit = Habit(activity["name"], activity["time_set"])   
                    print(self.username + ' ' + habit.habit_name)
class Login(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.io = DataIO.DataIO('.JSON/data.json')
        
    def userVerification(self):
        data = self.io.load_data()
    #    try:
    #        with open(file_path_user, 'r') as file:
    #            user_data = json.load(file)
    #    except FileNotFoundError:
    #        print("Error: File 'user.json' not found")
    #        return False
    #    except json.JSONDecodeError:
    #        print("Error: Failed to decode JSON from 'users.json'")
    #        return False

        for user in data:
            if self.username == user["username"] and self.password == user["password"]:
                super().setHabits()
                return True
            else: 
                return False
        #if self.username in user_data and user_data["password"] == self.password:
        #    self.authenticated = True
        #    return True
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
    def __init__(self, habit_name, habit_setting):
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
