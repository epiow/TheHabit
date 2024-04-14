import flet as ft
import View
import Database as db

import datetime
import calendar
from calendar import HTMLCalendar
from dateutil import relativedelta

database = db.Database('./JSON/data.json')

class FletCalendar(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        
        self.page = page
        self.get_current_date()
        self.set_theme()
        
        self.calendar_container = ft.Container(width=15000, height=850,
                                          padding=ft.padding.only(left=400, bottom=500), 
                                          border_radius=ft.border_radius.all(10),
                                          alignment=ft.alignment.bottom_center)
        self.build()
        self.output = ft.Text()

    def get_current_date(self):
        today = datetime.datetime.today()
        self.current_month = today.month
        self.current_day   = today.day
        self.current_year  = today.year 

    def get_next(self, e):
        '''Move to the next month.'''
        current = datetime.date(self.current_year, self.current_month, self.current_day) 
        add_month = relativedelta.relativedelta(months=1)
        next_month = current + add_month
        
        self.current_year = next_month.year
        self.current_month = next_month.month
        self.current_day = next_month.day
        self.build()
        self.calendar_container.update()
    
    def get_prev(self, e):
        '''Move to the previous month.'''
        current = datetime.date(self.current_year, self.current_month, self.current_day) 
        add_month = relativedelta.relativedelta(months=1)
        next_month = current - add_month
        self.current_year = next_month.year
        self.current_month = next_month.month
        self.current_day = next_month.day
        self.build()
        self.calendar_container.update()
        
    def get_calendar(self):
        '''Get the calendar from the calendar module.'''
        cal = HTMLCalendar()
        return cal.monthdayscalendar(self.current_year, self.current_month)
    
    def set_theme(self, text_color=ft.colors.BLACK):
        self.text_color = text_color
    
    def build(self):
        '''Build the calendar for flet.'''
        current_calendar = self.get_calendar()
        
        str_date = '{0}, {1}'.format(self.current_year, calendar.month_name[self.current_month])
        
        date_display = ft.Text(str_date, text_align='center', size=20, color=self.text_color)
        next_button = ft.Container( ft.Text('>', text_align='right', size=20, color=self.text_color), on_click=self.get_next, padding=ft.padding.only(left=280) )
        prev_button = ft.Container( ft.Text('<', text_align='left', size=20, color=self.text_color), on_click=self.get_prev, padding=ft.padding.only(left=70) )
        
        calendar_column = ft.Column([ft.Row([prev_button, date_display, next_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY, 
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER, height=40, expand=False)], 
                                    spacing=2, width=355, height=330, alignment=ft.MainAxisAlignment.START, expand=False)
        self.calendar_container.content = calendar_column
        return self.calendar_container

def calendarWindow(page: ft.Page):
    page.title = "Calendar Heatmap"
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


    mycal = FletCalendar(page)
    
    # Add to our application.
    user = "Aaron"
    page.add(
        ft.Column(
            [
                ft.Container(
                    ft.Text(
                        f"Welcome {user}!", size=50, color=ft.colors.BLACK, text_align=ft.TextAlign.RIGHT
                    ), padding=ft.padding.only(left=650), 
                ),
                mycal,
            ]
        )
    )


if __name__ == "__main__":
    ft.app(target=View.windowLogin)    
    #ft.app(target=View.login)