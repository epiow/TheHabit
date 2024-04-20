from View.viewProperties import UserColors as colors
def eventButtonOnHover(e):
    e.control.bgcolor = vars.set_transparency(colors.foreground, 0.1) if e.data == "true" else None
    e.control.update()
def eventToggleCrossOnClick(e):
    e.control.data = not e.control.data
    e.control.content.opacity = e.control.data
    e.control.update()
