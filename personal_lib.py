import json
import os

LIBRARY_FILE = 'library.json'


def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []


def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)


def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }

    library.append(book)
    save_library(library)
    print("Book added successfully!\n")


def view_books(library):
    if not library:
        print("Library is empty.\n")
        return

    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")
    print()


def search_books(library):
    keyword = input("Enter title or author to search: ").strip().lower()
    results = [book for book in library if keyword in book['title'].lower() or keyword in book['author'].lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")
    else:
        print("No matching books found.")
    print()


def update_book(library):
    view_books(library)
    try:
        index = int(input("Enter book number to update: ")) - 1
        if 0 <= index < len(library):
            print("Leave blank to keep existing value.")
            title = input(f"New title [{library[index]['title']}]: ").strip()
            author = input(f"New author [{library[index]['author']}]: ").strip()
            year = input(f"New year [{library[index]['year']}]: ").strip()
            genre = input(f"New genre [{library[index]['genre']}]: ").strip()

            if title:
                library[index]['title'] = title
            if author:
                library[index]['author'] = author
            if year:
                library[index]['year'] = year
            if genre:
                library[index]['genre'] = genre

            save_library(library)
            print("Book updated successfully!\n")
        else:
            print("Invalid book number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def delete_book(library):
    view_books(library)
    try:
        index = int(input("Enter book number to delete: ")) - 1
        if 0 <= index < len(library):
            removed = library.pop(index)
            save_library(library)
            print(f"Deleted '{removed['title']}' from library.\n")
        else:
            print("Invalid book number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def main():
    library = load_library()

    while True:
        print("==== Personal Library Manager ====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_books(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            update_book(library)
        elif choice == '5':
            delete_book(library)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
