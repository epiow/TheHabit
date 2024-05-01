from View.viewProperties import *
from View.viewWindowMain import *
from Model.modelClassData import *
from Model.modelClassData import *

#user = User("", "")

def eventButtonLoginClick(e: ft.ControlEvent):
    currentUsername = e.control.data[0].value
    currentPassword = e.control.data[1].value

    page: ft.Page = e.page
    vars: UserProperties = page.data[1]
    colors = vars.colors

    currentUserController = page.data[0]
    
    if(currentUserController.loginUser(currentUsername, currentPassword) != None):
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