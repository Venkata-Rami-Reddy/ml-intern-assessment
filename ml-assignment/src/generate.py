from src.ngram_model import TrigramModel

def main():
    model = TrigramModel()

    with open("data/example_corpus.txt", "r") as f:
        text = f.read()

    model.fit(text)
    print("Generated Text:")
    print(model.generate())

if __name__ == "__main__":
    main()

