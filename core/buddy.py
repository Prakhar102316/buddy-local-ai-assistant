from core.ollama_client import OllamaClient
from core.conversation import Conversation


class Buddy:

    def __init__(self):

        self.name = "Buddy"
        self.version = "0.2"

        self.client = OllamaClient()
        self.conversation = Conversation()

    def start(self):

        print("=" * 60)
        print(f"🤖 {self.name} v{self.version}")
        print("Type 'exit' to quit.")
        print("=" * 60)

        while True:

            user_input = input("\nYou : ")

            if user_input.lower() == "/clear":
                self.conversation.clear()
                print(self.conversation.get_messages())
                print("\nBuddy : Conversation cleared. 🧹")
                continue

            if user_input.lower() == "exit":
                print("\nBuddy : Goodbye Partner 👋")
                break

            # Store user message
            self.conversation.add_user_message(user_input)

            # Stream Buddy's response
            print("\nBuddy : ", end="", flush=True)

            full_response = ""

            for chunk in self.client.stream_generate(
                self.conversation.get_messages()
            ):
                print(chunk, end="", flush=True)
                full_response += chunk

            print()

            # Save assistant response
            self.conversation.add_assistant_message(full_response)
