from View.viewProperties import *
from View.viewWindowMain import *
from Model.modelClassData import *

currentUserData = Data()

def eventButtonLoginClick(e: ft.ControlEvent):
    f: ft.Page = e.control.data
    #f.window_close()
    
    currentUser = e.control.data[0].value
    currentUserPassword = e.control.data[1].value
    
    #print(currentUser, currentUserPassword)
    
    if(currentUserData.loginUser(currentUser, currentUserPassword) != None):
        #print(currentUserData.is_authenticated)
        return True
    else:
        #print(currentUserData.is_authenticated)
        return False
    

    #page: ft.Page = e.page
    #vars: UserProperties = page.data
    #colors = vars.colors
    #test = windowMain(page)
    #view = ft.View(controls=[test.stack], bgcolor=colors.background)
    #page.views.clear()
    #page.views.append(view)
    #page.update()

def eventButtonLoginHover(e):
    pass