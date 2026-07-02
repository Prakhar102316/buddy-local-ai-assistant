import flet as ft


def main(page: ft.Page):

    page.title = "Buddy AI"

    page.window.width = 1000
    page.window.height = 700

    page.theme_mode = ft.ThemeMode.DARK

    page.add(
        ft.Text(
            "Hello Partner! 🤖",
            size=28,
            weight=ft.FontWeight.BOLD
        )
    )


ft.app(target=main)