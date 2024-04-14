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
        if not self.findUser(username):
            new_user = User(username, password)
            self.users.append(new_user)
            return True
        return False
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
        self.currentActivity = None
        self.activities = []
    def createActivity(self, activity_name):
        if not self.findActivity(activity_name):
            new_activity = Activity(activity_name) 
            self.activities.append(new_activity)
    def findActivity(self, activity_name):
        activityFound = False
        for activity in self.activities:
            if activity.activity_name == activity_name:
                activityFound = True
                break
        return activityFound
    def editActivity(self, activity_name=""):
        nameSet = False
        if not self.findActivity(activity_name):
            if activity_name is not "":
                nameSet = True
                self.activities[self.currentActivity].name = activity_name
        return nameSet
    def deleteCurrentActivity(self):
        del self.activities[self.currentActivity]
        self.currentActivity = None
        

class Activity():
    def __init__(self, activity_name):
        self.name = activity_name
        self.currentEntry = None
        self.entries = []
    def createEntry(self, date_performed, time_set, time_elapsed, count):
        if self.findEntry(date_performed) is None:
            new_entry = ActivityEntry(date_performed, time_set, time_elapsed, count)
            self.entries.append(new_entry)
            return True
        return False
    def findEntry(self, date_performed):
        for entry in self.entries:
            if entry.date_performed == date_performed:
                return self.entries.index(entry)
        return None
    def editEntry(self, date_performed="", time_set="", time_elapsed="", count=""):
        dateSet = False
        timeSet = False
        elapsedSet = False
        countSet = False
        if not self.findEntry(date_performed):
            if date_performed is not "":
                dateSet = True
                self.entries[self.currentEntry].date_performed = date_performed
            if time_set is not "":
                timeSet = True
                self.entries[self.currentEntry].time_set = time_set
            if time_elapsed is not "":
                elapsedSet = True
                self.entries[self.currentEntry].time_elapsed = time_elapsed
            if count is not "":
                countSet = True
                self.entries[self.currentEntry].count = count
        return [dateSet, timeSet, elapsedSet, countSet]
                
    def deleteEnty(self):
        del self.entries[self.currentEntry]
        self.currentEntry = None
        
class ActivityEntry():
    def __init__(self, date_performed, time_set, time_elapsed, count):
        self.date_performed = date_performed
        self.time_set = time_set
        self.time_elapsed = time_elapsed
        self.count = count
