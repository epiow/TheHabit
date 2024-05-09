'''
def main():
    database = Data()
    database.login_user("mega@megaa.moe", "Pass123.")
    database.read_user_data()
    test = database.write_user_data()
    print(json.dumps(test,indent=4))
    x = UserProperties()
    page.data = [database, x]
    test = windowLogin(page)
    view = ft.View('login', controls=[test.stack], bgcolor='#FFe5e5e5')
    page.views.append(view)
    page.update()

if __name__ == "__main__":
    main()
'''
from View.viewWindowLogin import windowLogin
from View.viewWindowMain import windowMain

def main(page: ft.Page):
    page.title = "The Habit"

    def route_change(route):
        page.views.clear()
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [windowLogin(page)],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        elif page.route == "/main":
            page.views.append(
                ft.View(
                    "/main",
                    [windowMain(page)],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        else:
            # Handle other routes or display a default view
            page.views.append(
                ft.View(
                    "/",
                    [ft.Text("Default View")],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)
