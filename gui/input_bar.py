import flet as ft
from gui import styles


class InputBar(ft.Container):

    def __init__(self, send_callback):

        super().__init__()

        self.send_callback = send_callback

        self.input = ft.TextField(

            hint_text="Ask Buddy anything...",

            expand=True,

            border_radius=10,

            on_submit=self.send

        )

        self.button = ft.ElevatedButton(

            "Send",

            on_click=self.send

        )

        self.bgcolor = styles.INPUT_BAR

        self.padding = 15

        self.content = ft.Row(

            controls=[

                self.input,

                self.button

            ]

        )

    def send(self, e):

        text = self.input.value.strip()

        if text == "":

            return

        self.send_callback(text)

        self.input.value = ""

        self.update()