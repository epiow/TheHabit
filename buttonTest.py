import flet as ft

def main(page: ft.Page):
    buttonLogin = ft.Container(
        width= 154,
        height= 25,
        bgcolor= '#FF1bcf6e',
        border_radius=4,
        content= ft.Container(
            padding=6,
            content=ft.Text(
                'Login',
                font_family='Rockwell',
                color='#ffffff',
                weight='400',
                size=12,
                text_align=ft.TextAlign.CENTER
            )
        ),
        ink=True,
        on_click=lambda e: print("Clickable without Ink clicked!"),
    )
    
    page.add(buttonLogin)

ft.app(target=main)
