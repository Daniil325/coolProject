from flet import FilledButton, TextStyle, ButtonStyle, Page


class StartButton(FilledButton):

    def __init__(self, page):
        super().__init__(
            "Начать игру",
            icon="START",
            style=ButtonStyle(
                bgcolor="white",
                text_style=TextStyle(
                    size=30,
                    color="#376ed4"
                )
            ),
            width=300,
            height=100,
            on_click=self.start_click,
        )
        self.page = page

    def start_click(self, e):
        ...

