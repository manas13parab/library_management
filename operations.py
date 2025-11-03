from utils import generate_id

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    book_id = generate_id()

    book = {"id": book_id, "title": title, "author": author, "year": year}
    books.append(book)
    print("📚 Book added successfully!")

def view_books(books):
    if not books:
        print("No books found in the library.")
        return
    print("\n--- Library Books ---")
    for b in books:
        print(f"ID: {b['id']} | {b['title']} by {b['author']} ({b['year']})")