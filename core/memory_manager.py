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

    def get_all_memories(self):
        """
        Returns all saved memories as a dictionary.
        """
        return self.load_memory()
    def remember(self, key, value):

        memories = self.load_memory()

        memories[key] = value
 
        self.save_memory(memories)

    def forget(self, key):

        memories = self.load_memory()

        if key in memories:

            del memories[key]

            self.save_memory(memories)

            return True

        return False

    def edit(self, key, value):

        memories = self.load_memory()

        if key in memories:

            memories[key] = value

            self.save_memory(memories)

            return True

        return False
    def search_memory(self, query):
        memories = self.load_memory()

        results = {}

        query = query.lower()

        for key, value in memories.items():
            if query in key.lower() or query in str(value).lower():

                results[key] = value

        return results
