from pyrebase import pyrebase # Import pyrebase module for Firebase integration
from pyrebase_testing import Database
from datetime import datetime  # Import datetime module for date and time operations
from config import config_keys
from requests.exceptions import HTTPError
firebase = pyrebase.initialize_app(config_keys)

# Firebase database instance
db = Database()

def main():
    # Replace with actual email and password
    user_email = input("Create your email: ")
    user_password = input("Create your password: ")


    # Authenticate the user
    user = db.login_user(user_email, user_password)
    if user:
        print("User authentication successful")
        user_id = user['localId']  # Get the user ID from the authenticated user object
    except Exception as e:
        print("Error authenticating user:", e)
        return

        # Test activity creation
        print("\nTesting activity creation...")
        activity_name = input("Enter the activity name: ")
        time_set = input("Enter time of activity: ")
        time_elapsed = input("Enter duration of activity: ")

        # Use the user_uid for activity creation
        db.create_activity(user_uid, activity_name, time_set, time_elapsed)
    else:
        print("Authentication failed")

if __name__ == "__main__":
    main()