import flet as ft
from View.viewWindowLogin import *
from View.viewProperties import *
from View.viewWindowMain import *
from Model.modelClassData import *
import json
def main():
    database = Data()
    database.login_user("mega@megaa.moe", "Pass123.")
    database.read_user_data()
    test = database.write_user_data()
    print(json.dumps(test,indent=4))
'''
    x = UserProperties()
    page.data = [database, x]
    test = windowLogin(page)
    view = ft.View('login', controls=[test.stack], bgcolor='#FFe5e5e5')
    page.views.append(view)
    page.update()
'''
if __name__ == "__main__":
    main()