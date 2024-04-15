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
        if self.findUser(username) == None:
            new_user = User(username, password)
            self.users.append(new_user)
            return True
        return False
    def findUser(self, username):
        for user in self.users:
            if user.username == username:
                return self.users.index(user)
        return None
    def loginUser(self, username, password):
        userToLogin = self.findUser(username)
        if self.users[userToLogin].password == password:
            self.currentUser = userToLogin
            return True
        return False
    def editUser(self, username=None, password=None):
        usernameSet = False
        passwordSet = False
        if self.findUser(username) == None:
            if username != None:
                usernameSet = True
                self.users[self.currentUser].username = username
            if password != None:
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
        if self.findActivity(activity_name) == None:
            new_activity = Activity(activity_name) 
            self.activities.append(new_activity)
            return True
        return False
    def findActivity(self, activity_name):
        for activity in self.activities:
            if activity.activity_name == activity_name:
                return self.activities.index(activity)
        return None
    def setCurrentActivity(self, activity_name):
        activityToSet = self.findActivity(activity_name)
        if activityToSet != None:
            self.currentActivity = activityToSet
            return True
        return False
    def editActivity(self, activity_name=None):
        nameSet = False
        if self.findActivity(activity_name) == None:
            if activity_name != None:
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
        entryToIncrement = self.findEntry(date_performed)
        if entryToIncrement == None:
            new_entry = ActivityEntry(date_performed, time_set, time_elapsed, count)
            self.entries.append(new_entry)
            return True
        elif self.entryToIncrement.time_set == time_set:
            self.findEntry[entryToIncrement].count = count + 1
            return True
        return False
    def findEntry(self, date_performed):
        for entry in self.entries:
            if entry.date_performed == date_performed:
                return self.entries.index(entry)
        return None
    def editEntry(self, date_performed=None, time_set=None, time_elapsed=None, count=None):
        dateSet = False
        timeSet = False
        elapsedSet = False
        countSet = False
        if not self.findEntry(date_performed):
            if date_performed != None:
                dateSet = True
                self.entries[self.currentEntry].date_performed = date_performed
            if time_set != None:
                timeSet = True
                self.entries[self.currentEntry].time_set = time_set
            if time_elapsed != None:
                elapsedSet = True
                self.entries[self.currentEntry].time_elapsed = time_elapsed
            if count != None:
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
