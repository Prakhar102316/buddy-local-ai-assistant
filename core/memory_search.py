from core.memory_manager import MemoryManager


class MemorySearch:

    def __init__(self):
        self.memory = MemoryManager()

        self.stop_words = {
            "what", "who", "is", "are", "my", "me",
            "tell", "about", "do", "does", "did",
            "the", "a", "an", "please", "remember",
            "know", "which"
        }

        self.synonyms = {
            "favourite": "favorite",
            "fav": "favorite"
        }

    def normalize(self, word):

        word = word.lower()

        if word in self.synonyms:
            return self.synonyms[word]

        return word

    def get_keywords(self, text):

        words = []

        for word in text.lower().replace("?", "").split():

            word = self.normalize(word)

            if word not in self.stop_words:
                words.append(word)

        return words

    def get_relevant_context(self, query):

        memories = self.memory.load_memory()

        if not memories:
            return ""

        query_keywords = self.get_keywords(query)

        scored_memories = []

        for key, value in memories.items():

            key_words = key.replace("_", " ").split()

            key_words = [self.normalize(word) for word in key_words]

            score = 0

            for keyword in query_keywords:

                if keyword in key_words:
                    score += 2

                elif keyword in str(value).lower():
                    score += 1

            if score > 0:
                scored_memories.append((score, key, value))

        if not scored_memories:
            return ""

        scored_memories.sort(reverse=True)

        context = "Partner Information:\n\n"

        for _, key, value in scored_memories:

            readable_key = key.replace("_", " ").title()

            context += f"{readable_key}: {value}\n"

        return context