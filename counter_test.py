import flet as ft
import time


def main(page: ft.Page):

    page.title = "Counter Test"

    counter = ft.Text("0", size=40)

    page.add(counter)

    def tick():

        i = 0

        while True:

            i += 1

            counter.value = str(i)

            page.update()

            time.sleep(1)

    page.run_thread(tick)


ft.run(main)