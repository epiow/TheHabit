import flet as ft
import os
import Database
import View
import json

import json

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.authenticated = False

    def userVerification(self):
        folder_path = 'JSON'
        file_path_user = os.path.join(folder_path, 'user.json')
        try:
            with open(file_path_user, 'r') as file:
                user_data = json.load(file)
        except FileNotFoundError:
            print("Error: File 'user.json' not found")
            return False
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from 'users.json'")
            return False

        if self.username in user_data and user_data[self.username] == self.password:
            self.authenticated = True
            return True
        else:
            return False
            
        
class Register:
    #register function
    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def registerUser(self, user_data):
        if self.username in user_data:
            return False
        else:
            user_data[self.username] = self.password
            with open('user.json', 'w') as file:
                json.dump(user_data, file)
            return True 

'''
FOR REVISIONS

class Habit:
    def __init__(self, habit_name, habit_status_change, habit_delete):
        super().__init__()
        self.completed = False
        self.habit_name = habit_name
        self.habit_status_change = habit_status_change
        self.habit_delete = habit_delete

    def build(self):
        self.display_habit = ft.Checkbox(
            value=False, label=self.habit_name, on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_habit,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    async def edit_clicked(self, e):
        self.edit_name.value = self.display_habit.label
        self.display_view.visible = False
        self.edit_view.visible = True
        await self.update_async()

    async def save_clicked(self, e):
        self.display_habit.label = self.edit_name.value

class Calendar:
    def __init__(self, calendar_name, calendar_status_change, calendar_delete):
        super().__init__()
        self.completed = False
        self.calendar_name = calendar_name
        self.calendar_status_change = calendar_status_change
        self.calendar_delete = calendar_delete

    def build(self):
        self.display_calendar = ft.Checkbox(
            value=False, label=self.calendar_name, on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_calendar,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    async def edit_clicked(self, e):
        self.edit_name.value = self.display_calendar.label
        self.display_view.visible = False
        self.edit_view.visible = True
        await self.update_async()

    async def save_clicked(self, e):
        self.display_calendar.label = self.edit_name.value
'''