import flet as ft
import os
import DataIO
import Database
import json
class Data():
    def __init__(self, file_path):
        self.file_path = file_path
        self.currentUser = None
        self.users = []
    def createUser(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
    def findUser(self, username):
        userFound = False
        for user in self.users:
            if user.username == username:
                userFound = True
                break
        return userFound
    def loginUser(self, username, password):
        userFound = False
        for user in self.users:
            if user.username == username and user.password == password:
                userFound = True
                self.currentUser = self.users.index(user)
                break
        return userFound
    def editUser(self, username="", password=""):
        usernameSet = False
        passwordSet = False
        if not self.findUser(username):
            if username is not "":
                usernameSet = True
                self.users[self.currentUser].username = username
            if password is not "":
                passwordSet = True
                self.users[self.currentUser].password = password
        return [usernameSet, passwordSet]
    def deleteCurrentUser(self):
        del self.users[self.currentUser]
        self.currentUser = None
    
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.activities = []
    def createActivity(activity_name):
        

class Activity():
    def __init__(self, activity_name):
        self.name = activity_name
        self.entries = []
    def setEntries(self, times_performed):
        for entry in times_performed:
            new_entry = ActivityEntry(entry["date_performed"], entry["time_set"], entry["time_elapsed"], entry["count"])
            self.entries.append(new_entry)
    def addEntry(self, date_performed, time_set, time_elapsed, count):
        new_entry = ActivityEntry(date_performed, time_set, time_elapsed, count)
        for entry in self.entries:
            if(new_entry.date_performed == entry.date_performed):
                return False
        self.entries.append(new_entry)
        
class ActivityEntry():
    def __init__(self, date_performed, time_set, time_elapsed, count):
        self.date_performed = date_performed
        self.time_set = time_set
        self.time_elapsed = time_elapsed
        self.count = count
