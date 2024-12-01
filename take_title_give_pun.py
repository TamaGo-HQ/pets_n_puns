import json


# Load book data from the JSON file
try:
    with open("books_db.json", "r") as file:
        books = json.load(file)
except FileNotFoundError:
    print("Error: The books.json file is missing. Make sure the file exists.")
    books = {}

# Prompt the user for a book title
title = input("Enter the title of a book: ")

# Search for the book in the dictionary
if title in books:
    book_info = books[title]
    print(f"\nTitle: {title}\nAuthor: {book_info['author']}\nGenre: {book_info['genre']}")
    print(f"Sea Turtle Pun: {book_info['sea_turtle_pun']}")
    print(f"Cat Pun: {book_info['cat_pun']}")
else:
    print(f"\nSorry, I couldn't find the book '{title}' in the collection. 🐾🐢")