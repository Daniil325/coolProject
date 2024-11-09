import flet as ft


def main(page: ft.Page):
    page.theme = ft.theme.Theme(color_scheme_seed="white")
    page.bgcolor = "green"
    page.update()


ft.app(main)
