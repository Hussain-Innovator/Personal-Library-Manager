# Personal Library Manager

A clean and intuitive **Streamlit web application** for managing your personal book collection.  
Add, remove, search, view, and track reading progress of your books — with persistent storage using a local JSON file.

Built to demonstrate practical Python programming, file handling, data persistence, and modern UI development with Streamlit.

## Features

- Add new books with title, author, publication year, genre, and read/unread status
- Remove books by title
- Search books by title or author (case-insensitive partial matching)
- View complete list of books in a well-formatted table
- Track library statistics:
  - Total number of books
  - Reading progress percentage (books marked as read)
- Persistent data storage using `library.txt` (JSON format)
- Modern, responsive Streamlit interface with sidebar navigation, forms, and clear feedback

## Technologies Used

- Python 3
- Streamlit – for the web interface
- JSON – for structured data persistence
- Basic file I/O for reading/writing the library file

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Steps

1. Clone the repository

   ```bash
   git clone https://github.com/Hussain-lnnovator/Personal-Library-Manager.git
   cd Personal-Library-Manager

2. Project Structure:
Personal-Library-Manager/
├── library_manager.py       # Main Streamlit application
├── library.txt              # Data file (auto-created on first run)
└── README.md

Live Demo
A deployed version is available here:
https://personal-library-manager-jgqp2z2asfohprhydvr5nb.streamlit.app

Author:
Hussain
Software Engineer
hussainsamdanis686@gmail.com
