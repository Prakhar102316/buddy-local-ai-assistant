import flet as ft
import asyncio


async def main(page: ft.Page):

    page.title = "Async Counter"

    counter = ft.Text("0", size=40)

    page.add(counter)

    async def tick():

        i = 0

        while True:

            i += 1

            counter.value = str(i)

            page.update()

            await asyncio.sleep(1)

    page.run_task(tick)


ft.run(main)