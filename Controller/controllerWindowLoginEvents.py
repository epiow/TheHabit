from View.viewProperties import *
from View.viewWindowMain import *
from Model.modelClassData import *

user = User("", "")

def eventButtonLoginClick(e: ft.ControlEvent):
    currentUsername = e.control.data[0].value
    currentPassword = e.control.data[1].value

    currentUserController = Data()
    if(currentUserController.loginUser(currentUsername, currentPassword) != None):
        user = currentUserController.currentUser()
        page: ft.Page = e.page
        vars: UserProperties = page.data
        colors = vars.colors
        test = windowMain(page)
        print(currentUserController.currentUser.username)
        view = ft.View(controls=[test.stack], bgcolor=colors.background)
        page.views.clear()
        page.views.append(view)
        page.update()
    else:
        pass


def eventButtonLoginHover(e):
    pass