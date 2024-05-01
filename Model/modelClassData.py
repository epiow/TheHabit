from Model.modelClassUser import *
from Model.modelClassActivity import *
from Model.modelClassCalendar import *
from pyrebase import pyrebase
from datetime import datetime
from config import config_keys as keys

class Database:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()

class Data:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.currentUser = None
        self.users = []
        self.is_authenticated = False

    def createUser(self, username, password):
        try:
            self.auth.create_user_with_email_and_password(username, password)
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def findUser(self, username):
        for user in self.users:
            if user.username == username:
                return self.users.index(user)
        return None
    
    def loginUser(self, username, password):
        try:
            user = self.auth.sign_in_with_email_and_password(username, password)
            self.is_authenticated = True
            user_data = self.db.read_user_data(username)
            if user_data:
                self.currentUser = User(username, password)
                self.parse_user_data(user_data)
                return self.currentUser
            return None
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None

    def parse_user_data(self, user_data):
        for activity_name, activity_data in user_data.get("activities", {}).items():
            activity = Activity(activity_name)
            self.currentUser.activities.append(activity)
            for date_performed, entry_data in activity_data.get("date", {}).items():
                for entry_key, entry_values in entry_data.items():
                    for entry_value in entry_values:
                        entry = Entry(
                            entry_value.get("time_set"),
                            entry_value.get("time_elapsed"),
                            entry_value.get("count")
                        )
                        activity.entries.append(entry)
        self.currentUser.calendar = self.parse_calendar_data(user_data.get("calendar", {}))

    def parse_calendar_data(self, calendar_data):
        calendar = Calendar()
        for year_key, year_data in calendar_data.items():
            year = Year()
            for month_key, month_data in year_data.items():
                month = Month()
                for day_key, day_data in month_data.items():
                    day = Day()
                    for activity_key, activity_data in day_data.items():
                        activity = Activity(activity_key)
                        day.activities.append(activity)
                    month.weeks.append(day)
                year.months.append(month)
            calendar.years.append(year)
        return calendar
    
    def editUser(self, username=None, password=None):
        if self.currentUser is not None:
            if username is not None:
                self.currentUser.username = username
                self.db.set_name(username)
            if password is not None:
                self.currentUser.password = password
            return [username is not None, password is not None]
        return [False, False]

    def deleteCurrentUser(self):
        if self.currentUser is not None:
            self.db.delete_user(self.currentUser.username)
            del self.users[self.users.index(self.currentUser)]
            self.currentUser = None
            return True
        return False

    
