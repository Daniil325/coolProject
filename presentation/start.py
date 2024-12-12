from flet import Container

from .base import base_page
from presentation.components.start_button import StartButton


def start_page():
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    ct = Container()
    base_page(ct)
    ct.controls.append(StartButton(ct))
    return ct
