import pyrebase
from datetime import datetime
from config import config_keys as keys

class Database:


    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.is_authenticated = False

    def login_user(self, username, password):
        print(username)
        print(password)
        """
        Authenticate the user with the provided email and password.
        Args:
            username (str): User's email address.
            password (str): User's password.
        Returns:
            dict: User object if authentication is successful, None otherwise.
        """
        try:
            user = self.auth.sign_in_with_email_and_password(username, password)
            self.is_authenticated = True
            print("you are logged in")
            print(self.is_authenticated)
            return user
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None

    def create_user(self, username, password):
        """
        Create a new user with the provided email and password.
        Args:
            username (str): User's email address.
            password (str): User's password.
        Returns:
            bool: True if user creation is successful, False otherwise.
        """
        try:
            self.auth.create_user_with_email_and_password(username, password)
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def create_activity(self, user_id, activity_name, time_set, time_elapsed):
        """
        Create a new activity entry for the specified user.
        Args:
            user_id (str): ID of the user for whom the activity is recorded.
            activity_name (str): Name of the activity.
            time_set (str): Time when the activity was started.
            time_elapsed (str): Duration of the activity.
        Returns:
            None
        """
        today_date = datetime.today().strftime('%Y/%m/%d')
        data = {
            "time_set": time_set,
            "time_elapsed": time_elapsed,
            "count": 1
        }
        # Use the correct user_id in the path
        self.db.child("users").child(user_id).child("activities").child(activity_name).child(today_date).set(data)