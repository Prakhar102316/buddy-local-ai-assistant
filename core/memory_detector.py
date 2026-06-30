import re


class MemoryDetector:

    def detect(self, message):

        message = message.strip()

        patterns = [

            (
                r"my name is (.+)",
                "name"
            ),

            (
                r"my favourite superhero is (.+)",
                "favorite_superhero"
            ),

            (
                r"my favorite superhero is (.+)",
                "favorite_superhero"
            ),

            (
                r"my favourite fruit is (.+)",
                "favorite_fruit"
            ),

            (
                r"my favorite fruit is (.+)",
                "favorite_fruit"
            ),

            (
                r"i use (.+)",
                "operating_system"
            ),

            (
                r"i study (.+)",
                "education"
            )
        ]

        for pattern, key in patterns:

            match = re.match(pattern, message, re.IGNORECASE)

            if match:

                return {
                    "key": key,
                    "value": match.group(1).strip()
                }

        return None