from stats import count_chars
from stats import count_words

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    words = count_words(get_book_text())
    chars = count_chars(get_book_text())
    print(f"{words} words found in the document")
    print(chars)

main()
