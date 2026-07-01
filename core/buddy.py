from core.ollama_client import OllamaClient
from core.conversation import Conversation
from core.memory_manager import MemoryManager
from core.memory_detector import MemoryDetector
from core.ui import UI


class Buddy:

    def __init__(self):

        self.name = "Buddy"
        self.version = "0.6"

        self.client = OllamaClient()
        self.conversation = Conversation()

        self.memory = MemoryManager()
        self.detector = MemoryDetector()

    def start(self):

        UI.print_banner()

        while True:

            UI.user()
            user_input = input()

            if user_input.lower() == "/clear":
                self.conversation.clear()
                UI.success(
                    "Conversation cleared. Ready for a fresh start, Partner! 🧹"
                )
                continue

            if user_input.lower() == "/help":
                UI.show_help()
                continue

            if user_input.lower() == "/model":
                UI.show_model(self.client.model)
                continue

            if user_input.lower().startswith("/remember"):
                try:
                    data = user_input[len("/remember"):].strip()

                    key, value = data.split("=", 1)

                    key = key.strip().replace(" ", "_").lower()
                    value = value.strip()

                    self.memory.remember(key, value)

                    UI.success("Memory saved successfully. 🧠")
            
                except ValueError:
                     
                    UI.error("Usage: /remember key=value")

                continue
            if user_input.lower().startswith("/forget"):

                key = user_input[len("/forget"):].strip()

                key = key.replace(" ", "_").lower()

                deleted = self.memory.forget(key)

                if deleted:
                    UI.success("Memory removed successfully. 🗑️")
                else:
                    UI.error("Memory not found.")

                continue

            if user_input.lower().startswith("/edit"):

                try:

                    data = user_input[len("/edit"):].strip()

                    key, value = data.split("=", 1)

                    key = key.strip().replace(" ", "_").lower()
                    value = value.strip()

                    updated = self.memory.edit(key, value)

                    if updated:
                        UI.success("Memory updated successfully. ✏️")
                    else:
                        UI.error("Memory not found.")

                except ValueError:

                    UI.error("Usage: /edit key=value")

                continue


            if user_input.lower().startswith("/search"):

                query = user_input[len("/search"):].strip()

                results = self.memory.search_memory(query)

                UI.show_search_results(results)

                continue

            if user_input.lower() == "/stats":
                
                memories = self.memory.get_all_memories()

                total_memories = len(memories)

                total_messages = self.conversation.get_message_count()

                UI.show_stats(
                    total_memories,
                    total_messages,
                    self.version,
                    self.client.model
                )
                continue

            
            if user_input.lower() == "/memory":
                memories = self.memory.get_all_memories()
                UI.show_memory(memories)
                continue

            if user_input.lower() == "/about":
                UI.show_about(self.version)
                continue

            if user_input.lower() == "/version":
                UI.show_version(self.version)
                continue

            if user_input.lower() == "exit":
                UI.info("See you soon, Partner! 👋")
                break

            # -------- Memory Detection --------

            memory = self.detector.detect(user_input)

            if memory:

                memories = self.memory.load_memory()

                memories[memory["key"]] = memory["value"]

                self.memory.save_memory(memories)

            # -------------------------------

            self.conversation.add_user_message(user_input)

            memory_context = self.memory.get_memory_context()

            UI.buddy_prefix()

            full_response = ""

            for chunk in self.client.stream_generate(
                self.conversation.get_messages(memory_context)
            ):
                print(chunk, end="", flush=True)
                full_response += chunk

            print()

            self.conversation.add_assistant_message(full_response)