from ollama import chat


class OllamaClient:

    def __init__(self, model="buddy-fast"):
        self.model = model

    def generate(self, messages):
        print("\n========== MESSAGES SENT TO OLLAMA ==========")
        for message in messages:
            print(message)
        print("=============================================\n")

        response = chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]

    # -------------------------
    # NEW METHOD (Add this)
    # -------------------------

    def stream_generate(self, messages):

        print("\n========== MESSAGES SENT TO OLLAMA ==========")
        for message in messages:
            print(message)
        print("=============================================\n")

        stream = chat(
            model=self.model,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            yield chunk["message"]["content"]

