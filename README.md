# Personal Library Manager (Streamlit App)

A **Streamlit-powered** Personal Library Manager that allows users to manage their book collection through a user-friendly web interface.  
Built with Python, this app lets you add, remove, search, and view books while tracking statistics and storing data persistently using file handling.

---

## 🚀 Features

- **Add Books**: Enter title, author, publication year, genre, and mark as read/unread.
- **Remove Books**: Delete books by title.
- **Search Books**: Find books by title or author (case-insensitive).
- **View All Books**: Display a clean list of all books in your collection.
- **Statistics**: See total books and reading progress as a percentage.
- **File Handling**: All books are saved and loaded using a local `library.txt` file in JSON format.
- **Streamlit UI**: Modern interface with forms, sidebars, radio buttons, and styled outputs.

---

## Technologies Used

- **Python 3**
- **Streamlit** for UI
- **JSON File Handling** for saving and loading data

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Personal-Library-Manager.git
   cd Personal-Library-Manager
   ```bash
   https://personal-library-manager-jgqp2z2asfohprhydvr5nb.streamlit.app

2. Install dependencies:
pip install streamlit

# Running the App
streamlit run library_manager_streamlit.py

# Notes
Data Persistence: Books are stored in library.txt in the root directory. The file is automatically created if it doesn't exist.

Streamlit Forms are used for cleaner user input.

# Project Structure
Personal-Library-Manager/
│
├── library_manager.py
├── library.txt
└── README.md                      

# Author
Hussain
Final Year Software Engineering Student

📧 Email: hussainsamdanis686@gmail.com
📍 Karachi, Pakistan
