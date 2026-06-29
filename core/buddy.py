from core.ollama_client import OllamaClient


class Buddy:
    def __init__(self):
        self.name = "Buddy"
        self.version = "0.1"
        self.client = OllamaClient()

    def start(self):
        print(f"\n🤖 {self.name} v{self.version}")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("\nBuddy: Goodbye, Partner! 👋")
                break

            response = self.client.generate(user_input)

            print(f"\nBuddy: {response}\n")