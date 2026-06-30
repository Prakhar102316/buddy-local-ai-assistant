from core.prompt_manager import PromptManager


class Conversation:

    def __init__(self):

        self.prompt_manager = PromptManager()

        self.messages = [
            {
                "role": "system",
                "content": self.prompt_manager.get_system_prompt()
            }
        ]

    def add_user_message(self, message):
        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_assistant_message(self, message):
        self.messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def get_messages(self):
        return self.messages

    def clear(self):

        self.messages = [
            {
                "role": "system",
                "content": self.prompt_manager.get_system_prompt()
            }
        ]