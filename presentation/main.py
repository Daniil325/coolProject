import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors

from presentation.play import play_page
from presentation.start import start_page


def main(page: Page):
    page.title = "Routes Example"

    print("Initial route:", page.route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                   start_page()
                ],
            )
        )

        if page.route == "/settings":
            page.views.append(
                View(
                    "/settings",
                    [
                        play_page(page)
                    ],
                )
            )

        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_mail_settings(e):
        page.go("/settings/mail")

    def open_settings(e):
        page.go("/settings")

    page.go(page.route)
