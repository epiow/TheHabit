import flet as ft
from View.viewProperties import UserProperties
def main(page: ft.Page):
    vars                    = UserProperties()
    colors                  = vars.colors

    page.title              = "the Habit: Login"
    page.window_width       = vars.scale(286)
    page.window_height      = vars.scale(330)
    page.bgcolor            = colors.background
    page.window_resizable   = False

    def attempt_login()