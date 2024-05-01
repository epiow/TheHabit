import flet as ft
from viewProperties import *
def windowInsights(page: ft.Page):
    vars                    = UserProperties()
    colors                  = vars.colors

    page.title              = "the Habit: Login"
    page.window_width       = vars.scale(286)
    page.window_height      = vars.scale(220)
    page.bgcolor            = colors.background
    page.window_resizable   = False

    if page.platform is ft.PagePlatform.MACOS:
        page.window_title_bar_hidden = True

ft.app(target=windowInsights)
