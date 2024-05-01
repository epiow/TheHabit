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
        
        self.db.child("users").child(user_uid).child("activities").child(activity_name).child("date").child(str(year)).child("months").child(str(month)).child("days").child(str(day)).push(data)


    def read_activity(self, user_uid):
            activities = self.db.child("users").child(user_uid).child("activities").get()
            return activities.val()

    def update_activity(self, activity_name, date_performed, time_set, time_elapsed):
            user_id = self.user['uid']
            data = {
                "time_set": time_set,
                "time_elapsed": time_elapsed
            }
            self.db.child("users").child(user_id).child("activities").child(activity_name).child(date_performed).update(data)

    def delete_activity(self, activity_name, date_performed):
            user_id = self.user['uid']
            self.db.child("users").child(user_id).child("activities").child(activity_name).child(date_performed).remove()


class Calendar:
    def __init__(self, database):
        self.db = database

    def add_event(self, user_uid, event_name, event_date):
        pass

    def update_event(self, user_uid, event_name, new_event_date):
        pass

    def delete_event(self, user_uid, event_name):
        pass

class Timer:
    def start_timer(self):
        pass

    def pause_timer(self):
        pass

    def stop_timer(self):
        pass

class Notes:
    def add_note(self, user_uid, note_text):
        pass

    def update_note(self, user_uid, note_id, new_note_text):
        pass

    def delete_note(self, user_uid, note_id):
        pass
