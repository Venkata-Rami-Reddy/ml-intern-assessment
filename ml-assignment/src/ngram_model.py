import random
import re
from collections import defaultdict


class TrigramModel:
    def __init__(self):
        # trigram_counts[(w1, w2)][w3] = count
        self.trigram_counts = defaultdict(lambda: defaultdict(int))
        self.vocabulary = set()
        self.is_trained = False

    def clean_and_tokenize(self, text):
        # Lowercase and keep only words
        text = text.lower()
        tokens = re.findall(r"\b\w+\b", text)
        return tokens

    def fit(self, text):
        tokens = self.clean_and_tokenize(text)

        # Handle empty text case
        if not tokens:
            self.is_trained = False
            return

        # Pad with start and end tokens
        tokens = ["<s>", "<s>"] + tokens + ["</s>"]

        # Build trigram counts
        for i in range(len(tokens) - 2):
            w1, w2, w3 = tokens[i], tokens[i + 1], tokens[i + 2]
            self.trigram_counts[(w1, w2)][w3] += 1
            self.vocabulary.add(w3)

        self.is_trained = True

    def generate(self, max_length=50):
        # If no training happened → return empty string
        if not self.is_trained:
            return ""

        result = []
        w1, w2 = "<s>", "<s>"

        for _ in range(max_length):
            next_words = self.trigram_counts.get((w1, w2), None)

            # If context not found → stop
            if not next_words:
                break

            # Weighted random choice
            words, weights = zip(*next_words.items())
            w3 = random.choices(words, weights=weights)[0]

            if w3 == "</s>":
                break

            result.append(w3)

            # Move window
            w1, w2 = w2, w3

        return " ".join(result)


