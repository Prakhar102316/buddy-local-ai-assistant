import flet as ft
from gui import styles


class ChatArea(ft.Container):

    def __init__(self):

        super().__init__()

        self.messages = ft.ListView(
            expand=True,
            spacing=15,
            auto_scroll=True,
        )

        self.messages.controls.append(
            ft.Container(
                content=ft.Text(
                    "Hello Partner! 👋\n\nWelcome to Buddy AI",
                    color=styles.TEXT,
                    size=18,
                ),
                bgcolor=styles.BUDDY_MESSAGE,
                border_radius=12,
                padding=15,
                width=400,
            )
        )

        self.expand = True
        self.bgcolor = styles.CHAT_BACKGROUND
        self.padding = 20
        self.content = self.messages

    def add_user_message(self, text):

        bubble = ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.Container(
                    content=ft.Text(
                        text,
                        color=styles.TEXT,
                    ),
                    bgcolor=styles.USER_MESSAGE,
                    border_radius=12,
                    padding=15,
                )
            ],
        )

        self.messages.controls.append(bubble)

    def create_buddy_message(self):

        self.current_buddy_text = ft.Text(
            "",
            color=styles.TEXT,
        )

        bubble = ft.Row(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.Container(
                    content=self.current_buddy_text,
                    bgcolor=styles.BUDDY_MESSAGE,
                    border_radius=12,
                    padding=15,
                    width=400,
                )
            ],
        )

        self.messages.controls.append(bubble)

    def update_buddy_message(self, chunk):

        self.current_buddy_text.value += chunk