import random
import re
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        # (w1, w2) → {next_word: count}
        self.trigram_counts = defaultdict(lambda: defaultdict(int))
        self.vocab = set()
        self.is_trained = False

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # remove punctuation
        return text.split()

    def fit(self, text):
        if not text.strip():
            self.is_trained = False
            return

        tokens = self.clean_text(text)

        if len(tokens) < 2:
            self.is_trained = False
            return

        # Pad tokens
        tokens = ["<s>", "<s>"] + tokens + ["</s>"]

        # Count trigrams
        for i in range(len(tokens) - 2):
            w1, w2, w3 = tokens[i], tokens[i+1], tokens[i+2]
            self.trigram_counts[(w1, w2)][w3] += 1
            self.vocab.add(w3)

        self.is_trained = True

    def generate(self, max_length=50):
        if not self.is_trained:
            return ""

        w1, w2 = "<s>", "<s>"
        output = []

        for _ in range(max_length):
            next_words = self.trigram_counts.get((w1, w2), None)
            if not next_words:
                break

            # Convert counts to probabilities
            words = list(next_words.keys())
            counts = list(next_words.values())
            total = sum(counts)
            probabilities = [c / total for c in counts]

            next_word = random.choices(words, probabilities)[0]

            if next_word == "</s>":
                break

            output.append(next_word)

            w1, w2 = w2, next_word

        return " ".join(output)



