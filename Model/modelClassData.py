from modelClassUser import User
from modelClassActivity import Activity
from modelClassCalendar import Calendar, Year, Month, Day
from modelClassEntry import Entry
import pyrebase
import urllib.parse
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
                for activity_name, activity_entries in user_data["activities"].items():
                    self.currentUser.createActivity(activity_name)
                    self.currentUser.setCurrentActivity(activity_name)
                    currentActivity: Activity = self.currentUser.activities[self.currentUser.currentActivity]
                    for entry_key,entry_value in activity_entries["entries"].items():
                        currentActivity.createEntry(entry_value["date_performed"], entry_value["time_set"], entry_value["time_elapsed"], entry_value["count"])  
            else:
                print("No user data found for user:", user_id)
                return None
        except Exception as e:
            print(f"Error reading user data for user ID '{user_id}': {e}")
            return None

    def createUser(self, username, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        try:
            toChangeName = self.auth.sign_in_with_email_and_password(email,password)
            print(toChangeName["localId"])
            self.auth.update_profile(toChangeName["localId"], username)
            return self.loginUser(email, password)
        except Exception as e:
            print("Error")
            return False
    
    def loginUser(self, email, password):
        from requests.exceptions import HTTPError
        try:
            toLogin = self.auth.sign_in_with_email_and_password(email, password)
            self.currentUser = User(email, toLogin['localId'], toLogin['displayName'], password)
            return toLogin
        except HTTPError as e:
            print(f"Error authenticating user: {e.errno}")
            return None


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