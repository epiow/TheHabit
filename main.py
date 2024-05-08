import flet as ft
from View.viewWindowLogin import *
from View.viewProperties import *
from View.viewWindowMain import *
from Model.modelClassData import *

def main():
    database = Data()
    database.loginUser("mega@megaa.moe", "Pass123.")
    print(database.currentUser.username)
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