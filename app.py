import flet as ft

from presentation.main import main
from presentation.play import play_page


def app(page: ft.Page):
    play_page(page)


ft.app(target=app, assets_dir="assets")
