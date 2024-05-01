from View.viewProperties import *
from View.viewWindowLogin import *
def eventButtonOnHover(e):
    page: ft.Page = e.page
    vars: UserProperties = page.data[1]
    colors = vars.colors
    e.control.bgcolor = vars.set_transparency(colors.foreground, 0.1) if e.data == "true" else None
    e.control.update()
def eventToggleCrossOnClick(e):
    page: ft.Page = e.page
    vars: UserProperties = page.data[1]
    colors = vars.colors
    test = windowLogin(page)
    view = ft.View(controls=[test.stack], bgcolor=colors.background)
    page.views.clear()
    page.views.append(view)
    page.update()
    e.control.data = not e.control.data
    e.control.content.opacity = e.control.data
    e.control.update()
