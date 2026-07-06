import flet as ft
from gui.main_window import MainWindow

async def main(page: ft.Page):
    MainWindow(page)

ft.run(main)