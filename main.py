import flet as ft
import View
from backendController import Login
import Database as db

database = db.Database('./JSON/data.json')


if __name__ == "__main__":
    ft.app(target=View.login)