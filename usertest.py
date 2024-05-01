from pyrebase import pyrebase # Import pyrebase module for Firebase integration
from Model.modelFirebaseToPython import *
from datetime import datetime  # Import datetime module for date and time operations
from config import config_keys

import json
from Model.modelClassData import *
firebase = pyrebase.initialize_app(config_keys)

# Firebase database instance
db = Firebase()
local_user: User = 0
def main():
    # Replace with actual email and password

    user_email = "mega@megaa.moe"
    user_password = "Pass123."
    
    # Authenticate the user
    user = db.login_user(user_email, user_password)
    if user:
        print("User authentication successful")

        user_uid = user['localId'] 
        test: dict = db.read_activity(user_uid)
        print(json.dumps(test, indent=4, sort_keys=True))
        
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