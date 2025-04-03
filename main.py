from stats import count_chars
from stats import count_words
from stats import sort_dict

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    words = count_words(get_book_text())
    chars = count_chars(get_book_text())

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
