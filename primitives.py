import flet as ft
import os
def yo():
    print("yo")

UserColors = {
    "accent": "#1bcf6e",
    "background": "#e5e5e5",
    "foreground": "#D9000000",
    
}

def login(page: ft.Page):
    colors = UserColors
    page.title = "Login Example"
    page.window_width = 286*2
    page.window_height = 330*2
    page.bgcolor = colors["background"]
    svgLogo = ft.Image(
        src=os.path.join(os.getcwd(), "Assets/logo-big-full.svg"),
        fit=ft.ImageFit.FILL,
        width=198*2,
        height=110*2,
    )
    bgDots = ft.Image(
        src=os.path.join(os.getcwd(), "Assets/dots.svg"),
        fit=ft.ImageFit.FILL,
        width=page.window_width,
        height=page.window_height,
    )
    buttonLogin = ft.Container(
        content=ft.Container
        (
            ft.Text
            (
                "Login",
                font_family='Rockwell',
                color=page.bgcolor,
                weight='400',
                size=12*2
            ),
            alignment=ft.alignment.center,
            padding=8
        ),
        width= 154*2,
        height= 22*2,
        bgcolor= colors["accent"],
        border_radius=4*2,
        ink=True,
        on_click=yo
    )
    staticUsername = ft.Text(
        "Username",
        font_family='Rockwell',
        color='#000000',
        weight='400',
        size=12*2,
    )
    staticPassword = ft.Text(
        "Password",
        font_family='Rockwell',
        color='#000000',
        weight='400',
        size=12*2,
    )
    editUsername = ft.TextField(
        text_style= ft.TextStyle(
                font_family='Rockwell',
                color='#000000',
                weight='400',
                size=12*2,       
        ),
        border=ft.InputBorder.NONE,
        cursor_color='#7F1BCF6E',
        cursor_height=19*2,
        cursor_width=10,
        dense=True,
        width=242*2,
        height=22*2,
        bgcolor='#0D000000',
    )
    editPassword = ft.TextField(
        border=ft.InputBorder.NONE,
        text_style= ft.TextStyle(
                font_family='Rockwell',
                color='#000000',
                weight='400',
                size=12*2,       
        ),
        password=True,
        color='#000000',
        can_reveal_password=True,
        cursor_color='#7F1BCF6E',
        cursor_height=19*2,
        cursor_width=10,
        dense=True,
        width=242*2,
        height=22*2,
        bgcolor='#0D000000',
    )
    staticUsername = ft.Container(
        staticUsername,
        padding=8,
        left=22*2,
        top=154*2
    )
    staticPassword = ft.Container(
        staticPassword,
        padding=8,
        left=22*2,
        top=198*2
    )
    editUsername = ft.Container(
        editUsername,
        left=22*2,
        top=176*2
    )
    editPassword = ft.Container(
        editPassword,
        left=22*2,
        top=220*2
    )
    buttonLogin = ft.Container(
        buttonLogin,
        left=66*2,
        top=264*2
    )
    bgDots = ft.Container(
        bgDots,
        left=0,
        top=0,
        opacity=0.2
    )
    svgLogo = ft.Container(
        svgLogo,
        left=44*2,
        top=44*2,
    )
    stack = ft.Stack(
        [
            bgDots,
            svgLogo,
            staticUsername,
            staticPassword,
            editUsername,
            editPassword,
            buttonLogin
        ],

    )
    page.add(stack)
import os; print(os.getcwd())
ft.app(target=login)