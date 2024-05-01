from pyrebase import pyrebase # Import pyrebase module for Firebase integration
from pyrebase_testing import Database
from datetime import datetime  # Import datetime module for date and time operations
from config import config_keys
<<<<<<< HEAD
from requests.exceptions import HTTPError
=======
import json
from Model.modelClassData import *
>>>>>>> 68dede2 (pyrebase testing)
firebase = pyrebase.initialize_app(config_keys)

# Firebase database instance
db = Database()
local_user: User = 0
def main():
    # Replace with actual email and password
<<<<<<< HEAD
    user_email = input("Create your email: ")
    user_password = input("Create your password: ")


=======
    user_email = "mega@megaa.moe"
    user_password = "Pass123."
    
>>>>>>> 68dede2 (pyrebase testing)
    # Authenticate the user
    user = db.login_user(user_email, user_password)
    if user:
        local_user = User(user_email, user_password)
        print("User authentication successful")
<<<<<<< HEAD
        user_id = user['localId']  # Get the user ID from the authenticated user object
    except Exception as e:
        print("Error authenticating user:", e)
        return

=======
        user_uid = user['localId'] 
        test: dict = db.read_activity(user_uid)
        print(json.dumps(test, indent=4, sort_keys=True))
        
        
>>>>>>> 68dede2 (pyrebase testing)
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