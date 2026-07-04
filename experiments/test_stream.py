import flet as ft
import time


def main(page: ft.Page):

    page.title = "Streaming Test"

    output = ft.Text("", selectable=True)

    textbox = ft.TextField(width=400)

    def fake_stream():

        text = (
            "Hello Partner! This is a streaming test. "
            "If you see these words appearing one by one, "
            "then streaming works correctly."
        )

        for word in text.split():

            output.value += word + " "

            page.update()

            time.sleep(0.15)

    def send(e):

        output.value = ""

        page.update()

        # No thread
        fake_stream()

    page.add(
        textbox,
        ft.ElevatedButton(
            "Test Streaming",
            on_click=send,
        ),
        output,
    )


ft.app(target=main)