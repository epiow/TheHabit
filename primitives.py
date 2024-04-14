import flet as ft
import os

class UserColors:
    accent      = '#1BCF6E'
    background  = '#E5E5E5'
    foreground  = '#000000'

class UserProperties:
    scale_factor        = 2
    default_text_style  = ft.TextStyle(
                            font_family = 'Rockwell',
                            weight      = '400',
                            size        = 12 * scale_factor,
                        )
    textfield_style     = ft.TextStyle(
                            font_family = 'Rockwell',
                            weight      = '400',
                            size        = 12 * scale_factor,
                            color       = UserColors.foreground
                        )
    def scale(self,value):
        return value * self.scale_factor
    def set_transparency(self, value: str, alpha: float):
        return ('#' + hex(int(alpha * 255)).lstrip("0x") + value.lstrip("#")).upper()