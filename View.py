import flet as ft
import json
import Database
from backendController import User

def login(page: ft.Page):
    page.title = "Login Example"
    page.window_width = 285*2
    page.window_height = 319*2
    page.bgcolor ="#E5E5E5"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 80

    bg_img = ft.Image(
        src='./Assets/logo-big-mono.svg',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )
    
    def login_clicked(e):
        user = User(username.value, password.value)
        
        if user.loginUser() == True:
            dlg = ft.AlertDialog(
                title=ft.Text("Login Successful"),
                on_dismiss=lambda e: page.update(),
            )
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Login Failed"),
                on_dismiss=lambda e: page.update(),
            )

        page.dialog = dlg
        dlg.open = True
        page.update()
    
    username = ft.TextField(label="Username",color=ft.colors.BLACK)
    password = ft.TextField(label="Password", password=True, color=ft.colors.BLACK)


    
    buttonLogin = ft.Container(
            width= 266*2,
            height= 22*2,
            bgcolor= '#FF1bcf6e',
            alignment = ft.alignment.center,
            border_radius=4,
            content= ft.Container(
                padding=6,
                content=ft.Text(
                    'Login',
                    font_family='Rockwell',
                    color='#ffffff',
                    weight='400',
                    size=12*2,
                )
            ),
            ink=True,
            on_click=login_clicked,
    )

    page.add
    (

        ft.Container
        (
            ft.Column
            (
                [
                    ft.Container(bg_img, alignment=ft.alignment.center),
                    ft.Container(username),
                    ft.Container(password),
                    ft.Container(buttonLogin, alignment=ft.alignment.center),
                ]
            )
        )
    )
    

def registerWindow(page: ft.Page):

    page.title = "Register"
    page.bgcolor ="#E5E5E5"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 80

    bg_img = ft.Image(
        src=f"../Assets/logo-big-gray.svg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    def register_clicked(e):
        '''
        if username not in user.json
        register_new_user(username, password, file_path_user)

        else:
        print("Username already exists")
        '''

        try:
            if username.value in json.load(open('./JSON/user.json')):
                dlg = ft.AlertDialog(
                    title=ft.Text("Username already Exists"),
                    on_dismiss=lambda e: page.update(),
                )
            else:
                Register.registerUser(username.value, password.value)
                dlg = ft.AlertDialog(
                    title=ft.Text("Registration Successful"),
                    on_dismiss=lambda e: page.update(),
                )
        except Exception as e:
            dlg = ft.AlertDialog(
                title=ft.Text(f"An error occurred: {str(e)}"),
                on_dismiss=lambda e: page.update(),
            )

        page.dialog = dlg
        dlg.open = True
        page.update()
    
    username = ft.TextField(label="Username",color=ft.colors.BLACK)
    password = ft.TextField(label="Password", password=True, color=ft.colors.BLACK)
    confirm_password = ft.TextField(label="Confirm Password", password=True, color = ft.colors.BLACK)

    
    buttonLogin = ft.Container(
            width= 180,
            height= 50,
            bgcolor= '#FF1bcf6e',
            border_radius=4,
            alignment = ft.alignment.center,
            content= ft.Container(
                padding=6,
                content=ft.Text(
                    'Create Account',
                    font_family='Rockwell',
                    color='#dadada',
                    weight='400',
                    size=12,
                )
            ),
            ink=True,
            on_click=register_clicked,
    )

    page.add(ft.Container(
        ft.Column(
            [
                ft.Container(bg_img),
                ft.Container(username),
                ft.Container(password),
                ft.Container(confirm_password),
                ft.Container(buttonLogin),
            ],
            alignment=ft.alignment.center
        ),
        padding=20,
    )
    )

def habitWindow(page: ft.Page):

    page.add(
        ft.Column()
    )
