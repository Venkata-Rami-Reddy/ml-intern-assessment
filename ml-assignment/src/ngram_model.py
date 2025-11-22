
import random
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        self.trigrams = defaultdict(list)
        self.words = []

    def fit(self, text: str):
        # If empty text
        if not text:
            self.words = []
            self.trigrams = defaultdict(list)
            return

        # Split words
        self.words = text.split()

        # If less than 3 words, cannot form trigrams → tests expect generate() to still return a string
        if len(self.words) < 3:
            # No trigrams possible
            self.trigrams = defaultdict(list)
            return

        # Build trigrams
        for i in range(len(self.words) - 2):
            key = (self.words[i], self.words[i + 1])
            self.trigrams[key].append(self.words[i + 2])

    def generate(self) -> str:
        # Case 1: Empty text given
        if not self.words:
            return ""  # test expects empty string

        # Case 2: Less than 3 words → just return the original text
        if len(self.words) < 3:
            return " ".join(self.words)

        # Pick a random starting point
        start = random.choice(list(self.trigrams.keys()))
        w1, w2 = start
        generated = [w1, w2]

        # Generate next words
        for _ in range(20):  # small limit for safety
            key = (w1, w2)
            if key not in self.trigrams:
                break
            w3 = random.choice(self.trigrams[key])
            generated.append(w3)
            w1, w2 = w2, w3

        return " ".join(generated)




