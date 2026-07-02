from core.ollama_client import OllamaClient
from core.conversation import Conversation
from core.memory_manager import MemoryManager
from core.memory_search import MemorySearch
from core.question_classifier import QuestionClassifier


class BuddyBackend:

    def __init__(self):

        self.client = OllamaClient()

        self.conversation = Conversation()

        self.memory = MemoryManager()

        self.search = MemorySearch()

        self.classifier = QuestionClassifier()

    def ask(self, user_input):

        intent = self.classifier.classify(user_input)

        if intent == "PERSONAL":
            memory_context = self.search.get_relevant_context(user_input)
        else:
            memory_context = ""

        self.conversation.add_user_message(user_input)

        response = self.client.generate(
            self.conversation.get_messages(memory_context)
        )

        self.conversation.add_assistant_message(response)

        return response

    # -------------------------
    # NEW STREAMING METHOD
    # -------------------------

    def stream_ask(self, user_input):

        intent = self.classifier.classify(user_input)

        if intent == "PERSONAL":
            memory_context = self.search.get_relevant_context(user_input)
        else:
            memory_context = ""

        self.conversation.add_user_message(user_input)

        full_response = ""

        for chunk in self.client.stream_generate(
            self.conversation.get_messages(memory_context)
        ):

            full_response += chunk

            yield chunk

        self.conversation.add_assistant_message(full_response)