from modelClassUser import User
from modelClassActivity import Activity
from modelClassCalendar import Calendar, Year, Month, Day
from modelClassEntry import Entry
import pandas as pd
import numpy as np
import pyrebase
import urllib.parse
import json
from config import config_keys as keys

class Data:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.currentUser: User = None
    def read_user_data(self):
        user_id = self.currentUser.token_id
        try:
            if True:
                user_data = self.db.child("users").child(user_id).get().val()
                for activity_name, activity_entries in user_data.items():
                    self.currentUser.createActivity(activity_name)
                    self.currentUser.setCurrentActivity(activity_name)
                    currentActivity: Activity = self.currentUser.activities[self.currentUser.currentActivity]
                    for date_performed,entry_value in activity_entries.items():
                        currentActivity.createEntry(date_performed, entry_value["time_set"], entry_value["time_elapsed"], entry_value["count"], entry_value["notes"])  
            else:
                print("No user data found for user:", user_id)
                return None
        except Exception as e:
            print(f"Error reading user data for user ID '{user_id}': {e}")
            return None
    def write_user_data(self):
        data = {}
        user_id = self.currentUser.token_id
        activities = self.get_activities_list()  # Get the list of activities
        for activity in self.currentUser.activities:
            data[activity.activity_name] = {}
            for entry in activity.entries:
                entry_to_write = {
                    "count": entry.count,
                    "time_elapsed": entry.time_elapsed,
                    "time_set": entry.time_set,
                    "notes": entry.notes
                }
                data[activity.activity_name][entry.date_performed] = entry_to_write

        # Check if activity exists, if not, create a new one
        for activity_name in activities:
            if activity_name not in data:
                new_activity = Activity(activity_name)
                self.currentUser.activities.append(new_activity)
                data[activity_name] = {}

        self.db.child("users").child(user_id).update(data)
        return data
    def get_activities_list(self):
        if self.currentUser is not None:
            return [activity.activity_name for activity in self.currentUser.activities]
        else:
            return None
    def print_activities_on_canvas(self, canvas, x, y_start):
        activities = self.get_activities_list()
        if activities:
            for index, activity in enumerate(activities):
                y = y_start + index * 29.5  # Adjust the spacing between activities as needed
                canvas.create_text(
                    x,
                    y,
                    text=activity,
                    fill="#000000",
                    font=("Rockwell", 15)
                )
    def create_user(self, username, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        try:
            toChangeName = self.auth.sign_in_with_email_and_password(email,password)
            print(toChangeName["localId"])
            self.auth.update_profile(toChangeName["localId"], username)
            return self.login_user(email, password)
        except Exception as e:
            print("Error")
            return False
   
    def login_user(self, email, password):
        from requests.exceptions import HTTPError
        try:
            toLogin = self.auth.sign_in_with_email_and_password(email, password)
            self.currentUser = User(email, toLogin['localId'], toLogin['displayName'], password)
            self.read_user_data()
            return toLogin  
        except HTTPError as e:
            print(f"Error authenticating user: {e.errno}")
            return None
    def get_heatmap_data(self):
        start_date = None
        heatmap_data: list = []
        for activity in self.currentUser.activities:
            heatmap_data.append(activity.calculateHeatmap())
        return heatmap_data
    def editUser(self, username=None, password=None):
        if self.currentUser is not None:
            if username is not None:
                self.currentUser.username = username
                self.db.child("users").child(self.currentUser.username).update({"username": username})
            if password is not None:
                self.currentUser.password = password
            return [username is not None, password is not None]
        return [False, False]

    def deleteCurrentUser(self):
        if self.currentUser is not None:
            try:
                self.auth.delete_user(self.currentUser.email, self.currentUser.password)
                self.db.child("users").child(self.currentUser.username).remove()
                self.users.remove(self.currentUser)
                self.currentUser = None
                return True
            except Exception as e:
                print(f"Error deleting user: {e}")
                return False
