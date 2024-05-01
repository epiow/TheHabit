<<<<<<< HEAD

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
        
        # Display user activities
        for activity in user.activities:
            print("\nActivity:", activity.activity_name)
            print("Entries:")
            for entry in activity.entries:
                print("- Date performed:", entry.date_performed)
                print("  Time set:", entry.time_set)
                print("  Time elapsed:", entry.time_elapsed)
                print("  Count:", entry.count)

        # Display user's calendar
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
=======
import flet as ft
from View.viewWindowLogin import *
from View.viewProperties import *
from View.viewWindowMain import *
def main(page: ft.Page):
    page.data = UserProperties()
    test = windowLogin(page)
    view = ft.View('login', controls=[test.stack], bgcolor='#FFe5e5e5')
    page.views.append(view)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main)
>>>>>>> 587621ebb70b28c25fc65e384a8e16562c31972f
