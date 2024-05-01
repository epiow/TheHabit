import flet as ft
from Model.modelClassData import *

def eventButtonLoginClick(e: ft.ControlEvent):
    f: ft.Page = e.control.data
    #f.window_close()
    
    currentUser = e.control.data[0].value
    currentUserPassword = e.control.data[1].value
    
def eventButtonLoginHover(e):
    pass