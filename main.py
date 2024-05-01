import flet as ft
from View.viewWindowLogin import *
from View.viewWindowMain import *

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(route):
        page.add(ft.Text(f"New route: {route}"))

    def go_main(e):
        page.go(windowLogin(page))
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Go to Main", on_click=go_main))

if __name__ == '__main__':
    ft.app(target=main)