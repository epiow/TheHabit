import pyrebase
from datetime import datetime
from config import config_keys as keys

class Database:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.is_authenticated = False
        self.user = None

    def login_user(self, username, password):
        try:
            user = self.auth.sign_in_with_email_and_password(username, password)
            self.is_authenticated = True
            return user
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None

    def create_user(self, username, password):
        try:
            self.auth.create_user_with_email_and_password(username, password)
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def set_name(self, name):
        if self.user:
            user_id = self.user['uid']
            data = {"name": name}
            self.db.child("users").child(user_id).update(data)

    def create_activity(self, user_uid, activity_name, time_set, time_elapsed):
        today_date = datetime.today()
        year = today_date.year
        month = today_date.month
        day = today_date.day
        
        data = {
            "time_set": time_set,
            "time_elapsed": time_elapsed,
            "count": 1  
        }
        
        print(self.db.child("test").set(user_uid))

    def read_activity(self, user_uid):
            activities = self.db.child("users").child(user_uid).get()
            return activities.val()

    def update_activity(self, activity_name, date_performed, time_set, time_elapsed):
        if self.user:
            user_id = self.user['uid']
            data = {
                "time_set": time_set,
                "time_elapsed": time_elapsed
            }
            self.db.child("users").child(user_id).child("activities").child(activity_name).child(date_performed).update(data)

    def delete_activity(self, activity_name, date_performed):
        if self.user:
            user_id = self.user['uid']
            self.db.child("users").child(user_id).child("activities").child(activity_name).child(date_performed).remove()