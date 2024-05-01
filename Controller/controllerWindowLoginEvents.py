import flet as ft
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
    


def eventButtonLoginHover(e):
    pass