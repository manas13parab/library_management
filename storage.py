import json

FILE_NAME = "books.json"

def save_data(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []