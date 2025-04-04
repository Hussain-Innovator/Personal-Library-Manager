import streamlit as st
import json
import os

FILE_NAME = "library.txt"

# Load books from file
def load_books():
    if not os.path.exists("library.txt") or os.path.getsize("library.txt") == 0:
        return []  # Return empty list if file doesn't exist or is empty
    with open("library.txt", "r") as file:
        return json.load(file)

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book(books, title, author, year, genre, read):
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    books.append(new_book)
    save_books(books)
    st.success(f"Book '{title}' added successfully!")

# Remove a book
def remove_book(books, title):
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            st.success(f"Book '{title}' removed successfully!")
            return
    st.warning("Book not found.")

# Search books by title or author
def search_books(books, keyword):
    results = [book for book in books if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
    return results

# Display a book card
def display_book(book):
    status = "Read" if book["read"] else "Unread"
    st.markdown(f"""
    **Title:** {book['title']}  
    **Author:** {book['author']}  
    **Year:** {book['year']}  
    **Genre:** {book['genre']}  
    **Status:** {status}
    ---
    """)

# Show statistics
def display_stats(books):
    total = len(books)
    read_count = sum(1 for book in books if book["read"])
    read_percentage = (read_count / total * 100) if total > 0 else 0
    st.info(f"**Total Books:** {total}")
    st.info(f"**Books Read:** {read_count}")
    st.info(f"**Read Percentage:** {read_percentage:.2f}%")

# App layout
def main():
    st.title("📚 Personal Library Manager")

    books = load_books()

    menu = ["Add Book", "Remove Book", "Search Book", "View All Books", "Library Stats"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Add Book":
        st.subheader("Add a New Book")
        with st.form("add_book_form"):
            title = st.text_input("Book Title")
            author = st.text_input("Author")
            year = st.number_input("Publication Year", min_value=0, max_value=9999, step=1)
            genre = st.text_input("Genre")
            read = st.radio("Have you read this book?", ["Yes", "No"]) == "Yes"
            submitted = st.form_submit_button("Add Book")
            if submitted:
                if title and author and genre:
                    add_book(books, title, author, year, genre, read)
                else:
                    st.error("Please fill all the fields.")

    elif choice == "Remove Book":
        st.subheader("Remove a Book")
        title = st.text_input("Enter the exact title of the book to remove")
        if st.button("Remove Book"):
            remove_book(books, title)

    elif choice == "Search Book":
        st.subheader("Search for a Book")
        keyword = st.text_input("Enter title or author to search")
        if keyword:
            results = search_books(books, keyword)
            if results:
                st.success(f"{len(results)} result(s) found:")
                for book in results:
                    display_book(book)
            else:
                st.warning("No books found with that keyword.")

    elif choice == "View All Books":
        st.subheader("Your Book Collection")
        if books:
            for book in books:
                display_book(book)
        else:
            st.info("Your library is currently empty.")

    elif choice == "Library Stats":
        st.subheader("Library Statistics")
        display_stats(books)

if __name__ == "__main__":
    main()
