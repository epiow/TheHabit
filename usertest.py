from pyrebase import pyrebase  # Import pyrebase module for Firebase integration
from pyrebase_testing import Database
from datetime import datetime  # Import datetime module for date and time operations
from config import config_keys

firebase = pyrebase.initialize_app(config_keys)

# Firebase authentication and database instances
auth = firebase.auth()
db = firebase.database()

def create_activity(user_id, activity_name, time_set, time_elapsed):
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
    try:
        # Write activity data to Firebase database
        db.child("users").child(user_id).child("activities").child(activity_name).child(today_date).set(data)
        print("Activity created successfully")
    except Exception as e:
        print("Error creating activity:", e)

def main():
    # Replace with actual email and password
    user_email = input("Create your email: ")
    user_password = input("Create your password: ")


    # Authenticate the user
    try:
        user = auth.sign_in_with_email_and_password(user_email, user_password)
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

    # Use the user_id for activity creation
    create_activity(user_id, activity_name, time_set, time_elapsed)

if __name__ == "__main__":
    main()