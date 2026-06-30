class PromptManager:

    def __init__(self):
        with open(
            "prompts/system_prompt.txt",
            "r",
            encoding="utf-8"
        ) as file:
            self.system_prompt = file.read()

    def get_system_prompt(self):
        return self.system_prompt