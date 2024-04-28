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
    colors = UserColorsLight()
    scale_factor        = 2
    default_top_left_margin = ft.margin.only(left=6, top=6)
    default_top_left_padding = ft.padding.only(left=6, top=6)
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
    logo_big_full       = 'logo-big-full-light.svg'
    dots_login          = 'dots-login-light.svg'
    def scale(self,value):
        return value * self.scale_factor
    def set_transparency(self, value: str, alpha: float):
        return ('#' + hex(int(alpha * 255)).lstrip("0x") + value.lstrip("#")).upper()

class UserControls:
    def Icon(src, fit, width, height):
        return ft.Image(
            src=src,
            fit=fit,
            width = width,
            height= height
        )
    