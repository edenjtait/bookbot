from stats import count_chars
from stats import count_words
from stats import sort_dict
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    words = count_words(book)
    chars = count_chars(book)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    sorted_chars = sort_dict(chars)
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
