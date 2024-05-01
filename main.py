from Model.modelClassData import *

# TESTING PART ON THIS POINT
def main():
    database = Data()
    username = "ami"
    email = "epiow@gmail.com"
    password = "password123"

    user = database.loginUser(email, password)  # Use 'database' instead of 'data'
    if user != False:
        print("User authentication successful!")
        print("Username:", user["displayName"])
        print("Email: ", user["email"])
        database.read_user_data()
        for i in database.currentUser.activities:
            print(i.activity_name)
            for j in i.entries:
                print(j.date_performed)
        '''
        for activity in user.activities:
            print("\nActivity:", activity.activity_name)
            print("Entries:")
            for entry in activity.entries:
                print("- Date performed:", entry.date_performed)
                print("  Time set:", entry.time_set)
                print("  Time elapsed:", entry.time_elapsed)
                print("  Count:", entry.count)

        
        print("\nCalendar:")
        for year in user.calendar.years:
            print("Year:")
            for month in year.months:
                print("Month:")
                for week in month.weeks:
                    print("Week:")
                    for day in week.days:
                        print("Day:")
                        for activity in day.activities:
                            print("- Activity:", activity.activity_name)
        '''
    else:
        print("User authentication failed.")

if __name__ == "__main__":
    main()
