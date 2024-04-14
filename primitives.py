import flet as ft
import os

class UserColorsLight:
    accent      = '#1BCF6E'
    background  = '#E5E5E5'
    foreground  = '#1D2833'
class UserColorsDark:
    accent      = '#CE1D6E'
    foreground  = '#E5E5E5'
    background  = '#1D2833'
class UserProperties:
    colors = UserColorsDark()
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
                            color       = colors.foreground
                        )
    logo_big_full       = 'logo-big-full-dark.svg'
    dots                = 'dots-dark.svg'
    def scale(self,value):
        return value * self.scale_factor
    def set_transparency(self, value: str, alpha: float):
        return ('#' + hex(int(alpha * 255)).lstrip("0x") + value.lstrip("#")).upper()