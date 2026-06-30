from core.ollama_client import OllamaClient
from core.conversation import Conversation
from core.memory_manager import MemoryManager
from core.memory_detector import MemoryDetector


class Buddy:

    def __init__(self):

        self.name = "Buddy"
        self.version = "0.3"

        self.client = OllamaClient()
        self.conversation = Conversation()

        self.memory = MemoryManager()
        self.detector = MemoryDetector()

    def start(self):

        print("=" * 60)
        print(f"🤖 {self.name} v{self.version}")
        print("Type 'exit' to quit.")
        print("=" * 60)

        while True:

            user_input = input("\nYou : ")

            if user_input.lower() == "/clear":
                self.conversation.clear()
                print("\nBuddy : Conversation cleared. 🧹")
                continue

            if user_input.lower() == "exit":
                print("\nBuddy : Goodbye Partner 👋")
                break

            # -------- Memory Detection --------

            memory = self.detector.detect(user_input)

            if memory:

                memories = self.memory.load_memory()

                memories[memory["key"]] = memory["value"]

                self.memory.save_memory(memories)

            # -------------------------------

            # Store user message in conversation
            self.conversation.add_user_message(user_input)

            # Load Buddy's long-term memory
            memory_context = self.memory.get_memory_context()
            
            print("\nBuddy : ", end="", flush=True)

            full_response = ""

            for chunk in self.client.stream_generate(
                self.conversation.get_messages(memory_context)
            ):
                print(chunk, end="", flush=True)
                full_response += chunk

            print()

            # Store assistant response
            self.conversation.add_assistant_message(full_response)
