from flet import Page

HEIGHT = 700
WIDTH = 1000


def base_page(page: Page) -> None:
    page.bgcolor = "green"
    page.window_resizable = False
    page.maximizable = False
    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.padding = 0
    page.margin = 0
    page.update()

