import random
import re
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        # trigram counts: (w1, w2) -> {w3: count}
        self.trigram_counts = defaultdict(lambda: defaultdict(int))
        self.vocab = set()

    def _clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

    def _tokenize(self, text):
        return text.split()

    def fit(self, text):
        """
        Trains the trigram model on the given text.
        """
        text = self._clean_text(text)
        tokens = self._tokenize(text)

        # pad with start and end tokens
        tokens = ["<s>", "<s>"] + tokens + ["</s>"]

        self.vocab.update(tokens)

        # count trigrams
        for i in range(len(tokens) - 2):
            w1, w2, w3 = tokens[i], tokens[i+1], tokens[i+2]
            self.trigram_counts[(w1, w2)][w3] += 1

    def _sample_next(self, context):
        """
        Given a context (w1, w2), sample next word based on trigram probabilities.
        """
        next_words = self.trigram_counts.get(context, None)

        if not next_words:
            return "</s>"

        words = list(next_words.keys())
        counts = list(next_words.values())
        total = sum(counts)

        probs = [c / total for c in counts]
        return random.choices(words, probs)[0]

    def generate(self, max_length=50):
        """
        Generate text from the trained trigram model.
        """
        w1, w2 = "<s>", "<s>"
        output = []

        for _ in range(max_length):
            w3 = self._sample_next((w1, w2))

            if w3 == "</s>":
                break

            output.append(w3)
            w1, w2 = w2, w3

        return " ".join(output)
