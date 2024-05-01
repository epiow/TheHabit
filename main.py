import flet as ft
from View.viewWindowLogin import *
from View.viewProperties import *
from View.viewWindowMain import *
from Model.modelClassData import *
def main(page: ft.Page):
    page.data = UserProperties()
    test = windowLogin(page)
    view = ft.View('login', controls=[test.stack], bgcolor='#FFe5e5e5')
    page.views.append(view)
    page.update()

    db = Data()
    #db.auth.
    
if __name__ == "__main__":
    ft.app(target=main)
