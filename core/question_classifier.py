class QuestionClassifier:

    def __init__(self):

        self.personal_keywords = [
            "my",
            "me",
            "mine",
            "i",
            "favorite",
            "favourite",
            "remember",
            "know about me",
            "who am i",
            "my name",
            "my age",
            "my game",
            "my movie",
            "my language",
            "my superhero",
            "my food"
        ]

    def classify(self, question):

        question = question.lower()

        for keyword in self.personal_keywords:

            if keyword in question:
                return "PERSONAL"

        return "GENERAL"