# Evaluation – Design Choices for the Trigram Language Model

This document summarizes the design choices made while implementing the Trigram Language Model.

---

## **1. How N-gram Counts Are Stored**
I used nested `defaultdict` structures:

```python
self.trigram_counts = defaultdict(lambda: defaultdict(int))
```

This maps `(word1, word2) -> {next_word: count}`, which:
- avoids key errors,
- automatically initializes counts,
- keeps the structure simple and efficient for counting and lookup.

I also maintain a vocabulary set to store unique tokens.

---

## **2. Text Cleaning, Padding, and Unknown Words**
### **Cleaning**
- Convert all text to lowercase for consistency.
- Remove punctuation using a regex:  
  `re.sub(r"[^a-zA-Z0-9\s]", "", text)`
- Split text into tokens using `.split()`.

### **Padding**
To form valid trigrams and mark sentence boundaries:
- Add `<s> <s>` at the start
- Add `</s>` at the end

Example:
```
<s> <s> this is a test sentence </s>
```

### **Unknown Words**
Since the assignment corpus is small, all tokens occur in training.  
Thus, I don't introduce an `<UNK>` token.  
This keeps the implementation simple and aligned with test requirements.

---

## **3. Generation Logic & Probabilistic Sampling**
The `generate()` method:

1. Starts generation from (`<s>`, `<s>`).
2. Looks up all possible next words.
3. Converts counts into probabilities:
   ```python
   probabilities = [count / total for count in counts]
   ```
4. Randomly samples the next word using:
   ```python
   random.choices(words, probabilities)
   ```
5. Stops when:
   - `</s>` is generated, or  
   - `max_length` is reached.

Finally, it returns a joined string of generated words.

If the model was trained on empty or insufficient text, it returns an empty string (`""`), which is required by tests.

---

## **4. Other Design Decisions**
- Use simple regex cleaning for predictability.
- Use `defaultdict` instead of manual dictionary handling.
- Ensure `fit()` gracefully handles:
  - empty text,
  - single-word text,
  - missing trigram contexts.
- Keep implementation readable and beginner-friendly.

---

This design ensures the model is:
- **simple**
- **predictable**
- **test-friendly**
- **easy to extend** for future improvements.
