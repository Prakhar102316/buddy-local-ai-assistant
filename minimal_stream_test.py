import flet as ft
import time


def main(page: ft.Page):

    page.title = "Minimal Streaming Test"

    output = ft.Text(size=20)

    def stream():

        words = (
            "Hello Partner this is a minimal streaming test "
            "Every word should appear one by one."
        ).split()

        output.value = ""

        page.update()

        for word in words:

            output.value += word + " "

            page.schedule_update()

            time.sleep(0.25)

    page.add(

        ft.ElevatedButton(

            "Start Streaming",

            on_click=lambda e: page.run_thread(stream)

        ),

        output,

    )


ft.app(main)