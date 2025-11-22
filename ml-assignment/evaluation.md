# Evaluation – Design Choices for Trigram Language Model

### 1. Storage of N-gram Counts
I used a nested `defaultdict` structure:
This provides:
- O(1) access for lookups
- automatic initialization of dictionaries
- clear separation of context (w1, w2) → next-word counts

### 2. Text Cleaning and Tokenization
I converted all text to lowercase and removed punctuation using regex.  
Tokenization was done via simple `split()` which is sufficient for this dataset.  
Padding with `<s>` and `</s>` tokens ensures:
- proper start-of-sentence prediction
- proper termination during generation

Two `<s>` tokens are added to allow the first trigram to form correctly.

### 3. Handling Unknown Words
Since the corpus is small, I added every seen token to a vocabulary set.  
If a context is unseen during generation, the model returns `</s>` to safely stop text generation.

### 4. Generation Strategy
Generation begins with the context:
At each step:
1. Retrieve trigram probability distribution for the current context.
2. Use `random.choices()` with normalized probabilities to sample the next word.
3. Shift context (w1 → w2, w2 → w3).

Generation stops when:
- `</s>` appears
- or max_length is reached

### 5. Other Design Decisions
- I used simple regex cleaning to avoid unnecessary complexity.
- Probabilities are computed on the fly during sampling — no need to store them.
- The code is modular (`_clean_text`, `_tokenize`, `_sample_next`) making it easy to test.
- All design choices prioritize clarity, efficiency, and satisfying `test_ngram.py`.

This approach produces a clean, readable, and fully functional trigram language model.
