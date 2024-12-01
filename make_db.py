import json
import os

def add_book(books_dict, title, author, cat_pun, sea_turtle_pun, genre):
    """Add a book with details to the books dictionary."""
    books_dict[title] = {
        "author": author,
        "cat_pun": cat_pun,
        "sea_turtle_pun": sea_turtle_pun,
        "genre": genre
    }

# Dictionary of books
books = {
    "The Thing About Jellyfish": {
        "author": "Ali Benjamin",
        "cat_pun": "This book whiskered me away to a sea of emotions.",
        "sea_turtle_pun": "A shellebration of life, love, and loss!",
        "genre": "Young Adult"
    },
    "Honey and Spice": {
        "author": "Bolu Babalola",
        "cat_pun": "A pawsitively charming tale with a sweet twist!",
        "sea_turtle_pun": "This book is fin-tastic and full of flavor!",
        "genre": "Romance"
    },
    "The Poppy War": {
        "author": "R. F. Kuang",
        "cat_pun": "A claw-some mix of strategy and magic.",
        "sea_turtle_pun": "A tide-turning tale of power and survival.",
        "genre": "Fantasy"
    },
    "1984": {
        "author": "George Orwell",
        "cat_pun": "Fur-midable and thought-provoking, this is the purrfect dystopia.",
        "sea_turtle_pun": "A deep dive into the currents of surveillance and control.",
        "genre": "Dystopian"
    },
    "The Book Thief": {
        "author": "Markus Zusak",
        "cat_pun": "A purr-spective on the power of words and resilience.",
        "sea_turtle_pun": "A timeless story that swims deep into the human spirit.",
        "genre": "Historical Fiction"
    },
    "The Kite Runner": {
        "author": "Khaled Hosseini",
        "cat_pun": "A meow-sterpiece of love and redemption.",
        "sea_turtle_pun": "A ripple-effect story of loyalty and forgiveness.",
        "genre": "Historical Fiction"
    },
    "Circe": {
        "author": "Madeline Miller",
        "cat_pun": "A purr-suasive retelling of a classic myth.",
        "sea_turtle_pun": "A wave-making journey of transformation and magic.",
        "genre": "Fantasy"
    }
}

add_book(
    books,
    title="The Nightingale",
    author="Kristin Hannah",
    cat_pun="This tale of bravery is purr-fection, with characters who fight like fierce felines.",
    sea_turtle_pun="A story of resilience that will have you swimming through tears and shell-bration.",
    genre="Historical Fiction"
)

add_book(
    books,
    title="Six of Crows",
    author="Leigh Bardugo",
    cat_pun="These cunning characters are claw-ver, sleek, and paws-itively thrilling!",
    sea_turtle_pun="This gang of misfits is turtle-y unstoppable—like a heist in the deep blue sea!",
    genre="Fantasy"
)

add_book(
    books,
    title="War and Peace",
    author="Leo Tolstoy",
    cat_pun="This book is a paw-some marathon, filled with characters that pounce off the page.",
    sea_turtle_pun="This epic tale is slow and steady, just like a sea turtle’s journey—worth every page.",
    genre="Historical Fiction"
)
'''
# Check the dictionary to ensure the entries are there
for title, details in books.items():
    print(f"Title: {title}")
    print(f"  Author: {details['author']}")
    print(f"  Cat Pun: {details['cat_pun']}")
    print(f"  Sea Turtle Pun: {details['sea_turtle_pun']}")
    print(f"  Genre: {details['genre']}")
    print("-" * 40)
'''
# Save the dictionary to a JSON file
with open("books.json", "w") as file:
    json.dump(books, file, indent=4)

file_path = os.path.abspath("books.json")
print(f"The file is stored at: {file_path}")

with open("books.json", "r") as file:
    books_from_file = json.load(file)

for title, details in books_from_file.items():
    print(f"Title: {title}")
    print(f"  Author: {details['author']}")
    print(f"  Cat Pun: {details['cat_pun']}")
    print(f"  Sea Turtle Pun: {details['sea_turtle_pun']}")
    print(f"  Genre: {details['genre']}")
    print("-" * 40)