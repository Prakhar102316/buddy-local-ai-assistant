import asyncio
import flet as ft

from gui.sidebar import Sidebar
from gui.chat_area import ChatArea
from gui.input_bar import InputBar
from gui import styles

from core.backend import BuddyBackend


class MainWindow:

    def __init__(self, page: ft.Page):

        self.page = page
        self.backend = BuddyBackend()

        self.configure_window()
        self.build_ui()

    def configure_window(self):

        self.page.title = styles.WINDOW_TITLE
        self.page.window.width = styles.WINDOW_WIDTH
        self.page.window.height = styles.WINDOW_HEIGHT

        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = styles.BACKGROUND
        self.page.padding = 0

    def build_ui(self):

        self.chat = ChatArea()

        sidebar = Sidebar()

        input_bar = InputBar(self.send_message)

        right_side = ft.Column(
            controls=[
                self.chat,
                input_bar,
            ],
            expand=True,
            spacing=0,
        )

        layout = ft.Row(
            controls=[
                sidebar,
                right_side,
            ],
            expand=True,
            spacing=0,
        )

        self.page.add(layout)

    def send_message(self, text):

        self.chat.add_user_message(text)
        self.page.update()

        self.chat.create_buddy_message()
        self.page.update()

        self.page.run_task(self.stream_response, text)

    async def stream_response(self, text):

        for chunk in self.backend.stream_ask(text):

            self.chat.update_buddy_message(chunk)

            self.page.update()

            await asyncio.sleep(0)