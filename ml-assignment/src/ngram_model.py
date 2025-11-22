import random
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        self.trigrams = defaultdict(list)
        self.start_words = []

    def fit(self, text: str):
        # Handle empty text
        if not text or len(text.split()) < 3:
            self.start_words = []
            self.trigrams = defaultdict(list)
            return

        words = text.split()

        # Collect start words
        self.start_words = [(words[i], words[i+1]) for i in range(len(words) - 2)]

        # Build trigram table
        for i in range(len(words) - 2):
            key = (words[i], words[i+1])
            self.trigrams[key].append(words[i+2])

    def generate(self):
        # If no data learned, return empty string
        if not self.start_words or not self.trigrams:
            return ""

        # Pick random starting pair
        current = list(random.choice(self.start_words))
        result = current.copy()

        # Generate next words
        for _ in range(20):  # limit length
            key = tuple(current)
            if key not in self.trigrams:
                break
            next_words = self.trigrams[key]
            next_word = random.choice(next_words)
            result.append(next_word)

            current = [current[1], next_word]

        return " ".join(result)

