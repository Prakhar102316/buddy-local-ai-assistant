import json
import os


class MemoryManager:

    def __init__(self):

        self.file_path = "buddy_memory.json"

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({}, file, indent=4)

    def load_memory(self):

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def save_memory(self, memory):

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(memory, file, indent=4)

    def get_memory_context(self):

        memories = self.load_memory()

        if not memories:
            return ""

        context = "Partner Information:\n\n"

        for key, value in memories.items():

            readable_key = key.replace("_", " ").title()

            context += f"{readable_key}: {value}\n"

        return context

