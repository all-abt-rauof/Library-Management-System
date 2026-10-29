from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "library-app-secret-key"

# In-memory storage: all book data is reset when the server restarts.
books = []
next_book_id = 1


@app.route("/")
def index():
    """Display all books."""
    return render_template("index.html", books=books)


@app.route("/add_book", methods=["POST"])
def add_book():
    """Add a new book to the in-memory collection."""
    global next_book_id

    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()

    if not title or not author:
        flash("Fill all fields.", "error")
        return redirect(url_for("index"))

    books.append({
        "id": next_book_id,
        "title": title,
        "author": author,
        "available": True
    })
    next_book_id += 1

    flash(f"'{title}' added successfully", "success")
    return redirect(url_for("index"))


@app.route("/borrow_book/<int:book_id>", methods=["POST"])
def borrow_book(book_id):
    """Mark an available book as borrowed."""
    book = next((b for b in books if b["id"] == book_id), None)

    if book is None:
        flash("Book not found.", "error")
    elif not book["available"]:
        flash(f"Book '{book['title']}' is already borrowed.", "error")
    else:
        book["available"] = False
        flash(f"'{book['title']}' borrowed", "success")

    return redirect(url_for("index"))


@app.route("/return_book/<int:book_id>", methods=["POST"])
def return_book(book_id):
    """Mark a borrowed book as available."""
    book = next((b for b in books if b["id"] == book_id), None)

    if book is None:
        flash("Book not found.", "error")
    elif book["available"]:
        flash(f"Book '{book['title']}' is already available.", "error")
    else:
        book["available"] = True
        flash(f"'{book['title']}' returned", "success")

    return redirect(url_for("index"))


@app.route("/check_availability", methods=["POST"])
def check_availability():
    """Check a book's availability by title."""
    title = request.form.get("title", "").strip()

    if not title:
        flash("Enter a book title to check availability.", "error")
        return redirect(url_for("index"))

    book = next((b for b in books if b["title"].lower() == title.lower()), None)

    if book is None:
        flash(f"'{title}' - Not Found.", "error")
    elif book["available"]:
        flash(f"'{book['title']}' - Available.", "success")
    else:
        flash(f"'{book['title']}' - Borrowed.", "borrowed")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
