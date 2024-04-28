import flet as ft
def eventButtonLoginClick(e: ft.ControlEvent):
    f: ft.Page = e.control.data
    f.window_close()
def eventButtonLoginHover(e):
    pass