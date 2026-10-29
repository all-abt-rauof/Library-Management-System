# Library Management System

A beginner-friendly Flask mini project for managing library books using in-memory storage.

## Features

- Add new books with title and author
- Display all books
- Borrow available books
- Return borrowed books
- Check book availability
- Flask flash messages shown as auto-hiding popup (toast) notifications
- Responsive HTML5/CSS3 interface
- Data stored in memory and reset when the server restarts

## Project Structure

library_app/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css

## Installation

Open a terminal inside the `library_app` folder and run:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open this URL in your browser:

http://127.0.0.1:5000/

## Optional Challenges

This project can later be extended with:

1. SQLite persistent storage
2. Edit and delete book functionality
3. Search/filter by title or author
4. More robust input validation
