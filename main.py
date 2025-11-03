from book_operations import add_book, view_books
from manage_books import search_book, delete_book
from storage import save_data, load_data

def main():
    books = load_data()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            delete_book(books)
        elif choice == '5':
            save_data(books)
            print("✅ Data saved! Exiting...")
            break
        else:
            print("❌ Invalid choice, try again!")

if _name_ == "_main_":
    main()