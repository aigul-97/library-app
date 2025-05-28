
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
BOOKS_FILE = "books.txt"

def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return [line.strip().split("|") for line in file]
    except FileNotFoundError:
        return []

def save_book(title, author, year):
    with open(BOOKS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{title}|{author}|{year}\n")

@app.route("/")
def index():
    books = load_books()
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    author = request.form["author"]
    year = request.form["year"]
    save_book(title, author, year)
    return redirect("/")

@app.route("/search")
def search():
    query = request.args.get("q", "")
    books = load_books()
    result = [book for book in books if query.lower() in book[0].lower()]
    return render_template("search.html", books=result, query=query)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
