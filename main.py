import flet as ft
import View
import Database as db
from pyrebase_testing import Database

if __name__ == "__main__":
    ft.app(target=View.windowLogin)  # Pass login callback
