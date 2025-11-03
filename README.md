# 🧾 README — Piyush’s Modules (`book_operations.py` & `manage_books.py`)

👨‍💻 **Author:** Piyush Raj Singh  
📘 **Project:** Library Management System  

---

## 📁 Overview
These modules form the **core of the Library Management System**, handling all major operations related to book management — adding, viewing, searching, and deleting books from the system.  

The modules ensure that the system maintains an organized collection of books, allowing users to interact easily through a console-based interface.

| File | Description |
|------|--------------|
| **book_operations.py** | Contains functions for adding, viewing, and searching books. |
| **manage_books.py** | Manages deletion and organization of book records. |

---

## ⚙️ 1. `book_operations.py`

This file provides essential functions for maintaining the library’s book data — including adding new books, listing all available books, and searching for specific titles or authors.  

It imports a utility function `generate_id()` from the `utils` module to assign a **unique ID** to every new book.

### 📜 Code:
```python
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
        print(f"ID: {b['id']} | {b['title']} by {b['author']} ({b['year']})")

def search_book(books):
    keyword = input("Enter title or author to search: ").lower()
    results = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]
    if results:
        print("\n--- Search Results ---")
        for b in results:
            print(f"{b['title']} by {b['author']} ({b['year']})")
    else:
        print("❌ No books found matching your search.")


🧩 Key Functions
# 🧩 Key Functions — `book_operations.py`

#🔹 add_book(books)
1.Purpose: Adds a new book entry to the system.  
Details: Takes user input for the **title**, **author**, and **year**, generates a **unique ID** using `generate_id()`, and appends the new entry to the book list.


# 🔹 view_books(books)
2.Purpose: Displays all stored books in the system.  
Details: Prints each book’s **ID**, **title**, **author**, and **year** in a clear, formatted list.  
If no books are available, it shows the message — *“No books found in the library.”*


#🔹 search_book(books)
3.Purpose: Searches for a book by **title** or **author**.  
Details: Filters through the book records to find matches with the entered keyword.  
If no match is found, it displays — “No books found matching your search.”


⚙️ 2. manage_books.py
This module helps maintain the integrity of the library by allowing users to delete books using their unique IDs.

📜 Code:
python
Copy code
def delete_book(books):
    book_id = input("Enter book ID to delete: ")
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            print("🗑 Book deleted successfully!")
            return
    print("No book found with that ID.")
    
🧩 Key Function
# 🔹 delete_book(books)
1.Purpose: Deletes a book from the system using its unique ID.  
Details: Searches for a book by the entered **ID** and removes it if found.  
If no matching ID exists, it displays the message — “No book found with that ID.”


📊 Functionality Summary
Operation	Module                   	Purpose
Add Book	book_operations.py	Create and store a new book entry
View Books	book_operations.py	Display all available books
Search Book	book_operations.py	Find books by title or author
Delete Book	manage_books.py 	Remove a book from the system by ID

🚀 Future Improvements
Implement persistent storage (e.g., using JSON or database files).
Add edit/update functionality for book details.
Introduce a GUI for better user interaction.
Display statistics such as total number of books, authors, and genres.

✅ Conclusion
These modules form the operational heart of the Library Management System — providing a structured and user-friendly way to manage library resources.
The clear and modular approach ensures the code is easy to maintain, expandable, and efficient for future scalability.

