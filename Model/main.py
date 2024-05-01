from modelClassData import *
#TESTING PART ON THIS POINT
def main():
    database = Data()
    data = Data("file_path", database)

    username = "epiow@gmail.com"
    password = "password123"

    user = data.loginUser(username, password)
    if user:
        print("User authentication successful!")
        print("Username:", user.username)
        print("Password:", user.password)
        
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

    else:
        print("User authentication failed.")

if __name__ == "__main__":
    main()