from View.viewProperties import *
from View.viewWindowMain import *


def eventButtonLoginClick(e: ft.ControlEvent):
    page: ft.Page = e.page
    vars: UserProperties = page.data
    colors = vars.colors
    test = windowMain(page)
    view = ft.View(controls=[test.stack], bgcolor=colors.background)
    page.views.clear()
    page.views.append(view)
    page.update()

def eventButtonLoginHover(e):
    pass