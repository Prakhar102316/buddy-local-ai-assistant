import flet as ft

from gui import styles


class Sidebar(ft.Container):

    def __init__(self):

        super().__init__()

        self.width = styles.SIDEBAR_WIDTH

        self.bgcolor = styles.SIDEBAR

        self.padding = 20

        self.content = ft.Column(

            controls=[

                ft.Text(
                    "🤖 Buddy AI",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=styles.ACCENT
                ),

                ft.Divider(),

                ft.Text("💬 Chat"),

                ft.Text("🧠 Memory"),

                ft.Text("⚙ Settings"),

                ft.Text("ℹ About")

            ],

            spacing=20

        )   