def search_book(books):
    keyword = input("Enter title or author to search: ").lower()
    results = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]
    if results:
        print("\n--- Search Results ---")
        for b in results:
            print(f"{b['title']} by {b['author']} ({b['year']})")
    else:
        print("❌ No books found matching your search.")

def delete_book(books):
    book_id = input("Enter book ID to delete: ")
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            print("🗑 Book deleted successfully!")
            return
    print("❌ No book found with that ID.")