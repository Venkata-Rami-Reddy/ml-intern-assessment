# Trigram Language Model

This assignment implements a simple Trigram Language Model for generating text based on a training corpus.

## 📌 How to Run the Code

### 1️⃣ Install required packages
From inside the `ml-assignment` folder, run:

```
pip install -r requirements.txt
```

### 2️⃣ Run the test suite (to validate your model)
```
pytest -vv
```

### 3️⃣ Train the model & generate text
To generate text using the example corpus:

```
python src/generate.py
```

This will:
- train the trigram model using `data/example_corpus.txt`
- print generated text to the console

## 📁 Project Structure

```
ml-assignment/
│── data/
│   └── example_corpus.txt
│── src/
│   ├── ngram_model.py
│   ├── utils.py
│   └── generate.py
│── tests/
│   └
