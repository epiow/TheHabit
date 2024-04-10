import flet as ft
import os
import DataIO
import Database
import json

class User():
    def __init__(self, username, password):
        self.io = DataIO.DataIO('./JSON/data.json')
        self.db = Database.Database(self.io)
        self.username = username
        self.password = password
        self.activities = []

    def setActivities(self):
        data = self.io.load_data()
        for user in data:
            if(self.username == user["username"]):
                print(user["activities"])
                self.activities = user["activities"]

    def loginUser(self):
        data = self.io.load_data()
        userExists = False
        for user in data:
            if self.username == user["username"] and self.password == user["password"]:
                userExists = True
                self.setActivities()
                break
        return userExists
            
    def registerUser(self):
        return self.db.create_user(self.username, self.password)

class Activity():
    def __init__(self, activity_name):
        self.name = activity_name
        self.entries = []
class ActivityEntry():
    def __init__(self, date_performed, time_set, time_elapsed, count):
        self.date_performed = date_performed
        self.time_set = time_set
        self.time_elapsed = time_elapsed
        self.count = count
    