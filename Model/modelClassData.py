from modelClassUser import User
from modelClassActivity import Activity
from modelClassCalendar import Calendar, Year, Month, Day
from modelClassActivity import Entry
import pyrebase
import urllib.parse
from config import config_keys as keys

class Data:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.currentUser = None
        self.users = []

    def read_user_data(self, user_id):
        try:
            user_data = self.db.child("users").child(user_id).get().val()
            if user_data:
                parsed_activities = {}
                activities = user_data.get("activities", {})
                for activity_id, activity_data in activities.items():
                    parsed_activity = {"activity_id": activity_id, "entries": []}
                    dates = activity_data.get("date", {})
                    for year, year_data in dates.items():
                        for month, month_data in year_data.get("months", {}).items():
                            for day in month_data.get("days", []):
                                if day is not None:
                                    for entry_id, entry_data in day.items():
                                        entry_details = entry_data.get("entry", entry_data)
                                        time_set = entry_details.get("time_set", "")
                                        time_elapsed = entry_details.get("time_elapsed", "")
                                        count = entry_details.get("count", "")
                                        # Ensure time_set exists before using it
                                        if time_set:
                                            parsed_activity["entries"].append({
                                                "entry_id": entry_id,
                                                "time_set": time_set,
                                                "time_elapsed": time_elapsed,
                                                "count": count
                                            })
                                        else:
                                            print(f"Missing 'time_set' attribute for entry {entry_id}")
                    parsed_activities[activity_id] = parsed_activity
                return parsed_activities
            else:
                print("No user data found for user:", user_id)
                return None
        except Exception as e:
            print(f"Error reading user data for user ID '{user_id}': {e}")
            return None


    def createUser(self, username, password):
        try:
            self.auth.create_user_with_email_and_password(username, password)
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def loginUser(self, username, password):
        try:
            user = self.auth.sign_in_with_email_and_password(username, password)
            self.is_authenticated = True
            user_id = user['localId']
            user_data = self.read_user_data(user_id)
            print(user_data)
            '''
            if user_data:
                self.currentUser = User(username, password)
                self.parse_user_data(user_data)
                return self.currentUser
            return None
            '''
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None

    def parse_user_data(self, user_data):
        if "activities" in user_data:
            for activity_name, activity_data in user_data["activities"].items():
                activity = Activity(activity_name)
                self.currentUser.activities.append(activity)
                if "date" in activity_data:
                    for year, year_data in activity_data["date"].items():
                        for month, month_data in year_data.get("months", {}).items():
                            for day, day_data in month_data.get("days", {}).items():
                                if day_data is not None:
                                    for entry_id, entry_data in day_data.get("entries", {}).items():
                                        entry_details = entry_data
                                        time_set = entry_details.get("time_set", "")
                                        time_elapsed = entry_details.get("time_elapsed", "")
                                        count = entry_details.get("count", "")
                                        if time_set:
                                            entry = Entry(
                                                date_performed="",  # You may need to adjust this
                                                time_set=time_set,
                                                time_elapsed=time_elapsed,
                                                count=count
                                            )
                                            activity.entries.append(entry)
                                        else:
                                            print(f"Missing 'time_set' attribute for entry {entry_id}")
        if "calendar" in user_data:
            self.currentUser.calendar = self.parse_calendar_data(user_data["calendar"])

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
