import flet as ft
import Database
from backendController import Login    

def login(page: ft.Page):
    page.title = "Login Example"
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
    
    def login_clicked(e):
        login_user = Login(username.value, password.value)
        if login_user.userVerification():
            dlg = ft.AlertDialog(
                title=ft.Text("Login Successful"),
                on_dismiss=lambda e: page.update(),
            )
            calendar()
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
            width= 180,
            height= 50,
            bgcolor= '#FF1bcf6e',
            border_radius=4,
            alignment = ft.alignment.center,
            content= ft.Container(
                padding=6,
                content=ft.Text(
                    'Login',
                    font_family='Rockwell',
                    color='#ffffff',
                    weight='400',
                    size=12,
                )
            ),
            ink=True,
            on_click=login_clicked,
    )

    page.add(ft.Container(
        ft.Column(
            [
                ft.Container(bg_img, alignment=ft.alignment.center),
                ft.Container(username),
                ft.Container(password),
                ft.Container(buttonLogin, alignment=ft.alignment.center),
            ]
        ),
        padding=20,
    )
)
    
def calendar(page: ft.Page):

    page.add(
        ft.Column()
    )