from viewProperties import *
from Controller.controllerWindowMainEvents import *
def windowMain(page: ft.Page):
    vars = UserProperties()
    colors = vars.colors

    page.title              = "the Habit: Login"
    page.window_width       = vars.scale(484)
    page.window_height      = vars.scale(396)
    page.bgcolor            = colors.background
    page.window_resizable   = False
    
    if page.platform is ft.PagePlatform.MACOS:
        page.window_title_bar_hidden = False
    page.window_title_bar_buttons_hidden = False
    bgDots = ft.Image(
        src=os.path.join(os.getcwd(), "Assets", 'dots-main-light.svg'),
        fit = ft.ImageFit.FILL,
        width = page.window_width,
        height = page.window_height
    )
    iconLeftArrow = lambda: ft.Image(
        src=os.path.join(os.getcwd(), "Assets", 'icon-left-arrow-light.svg'),
        fit = ft.ImageFit.FILL,
        width=vars.scale(22),
        height=vars.scale(22)
    )
    iconRightArrow = lambda: ft.Image(
        src=os.path.join(os.getcwd(), "Assets", 'icon-right-arrow-light.svg'),
        fit = ft.ImageFit.FILL,
        width=vars.scale(22),
        height=vars.scale(22)
    )
    iconCross = lambda: ft.Image(
        src=os.path.join(os.getcwd(), "Assets", 'icon-cross-light.svg'),
        fit=ft.ImageFit.FILL,
        width = vars.scale(22),
        height= vars.scale(22)
    )
    staticDatePicker = ft.Text(
        "2024, April",
        style=vars.default_text_style,
        color=colors.foreground
    )
    staticWelcomeUser = ft.Text(
        "Welcome, User!",
        style=vars.default_text_style,
        color=colors.foreground
    )
    bgDots = ft.Container(
        bgDots,
        opacity = 0.2,
        left=0,
        top=0
    )
    buttonLeftArrow = ft.Container(
        iconLeftArrow(),
        left=vars.scale(308),
        top=vars.scale(66),
        on_hover=eventButtonOnHover,
    )
    buttonRightArrow = ft.Container(
        iconRightArrow(),
        left=vars.scale(440),
        top=vars.scale(66),
        on_hover=eventButtonOnHover,
    )
    toggleCross = lambda: ft.Container(
        iconCross(),
        data=True,
        left=vars.scale(154),
        top=vars.scale(154),
        on_hover=eventButtonOnHover,
        on_click=eventToggleCrossOnClick
    )
    staticDatePicker = ft.Container(
        staticDatePicker,
        padding=ft.padding.only(top=6),
        width=vars.scale(110),
        height=vars.scale(22),
        left=vars.scale(330),
        top=vars.scale(66),
        alignment=ft.alignment.center
    )
    staticWelcomeUser = ft.Container(
        staticWelcomeUser,
        padding=ft.padding.only(right=6, top=6),
        width=vars.scale(154),
        height=vars.scale(22),
        left=vars.scale(308),
        top=vars.scale(44),
        alignment=ft.alignment.center_right

    )
    def crosses(count):
        items = []
        offset = 0
        for i in range(1, count + 1):
            newToggleCross = toggleCross()
            newToggleCross.left += vars.scale(offset)
            items.append(newToggleCross)
            offset += 22
        return items
    listCrosses = crosses(14)
    stack = ft.Stack(
        [
            bgDots,
            buttonLeftArrow,
            buttonRightArrow,
            staticDatePicker,
            staticWelcomeUser
        ] + listCrosses
    )
    page.add(stack)

ft.app(target=windowMain)