import flet as ft

from gui.main_window import MainWindow


def main(page: ft.Page):

    MainWindow(page)


ft.app(target=main)