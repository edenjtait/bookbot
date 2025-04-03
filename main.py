def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(book):
    count  = 0
    words = book.split()
    for w in words:
        count += 1
    return count

def main():
    words = count_words(get_book_text())
    print(f"{words} words found in the document")

main()
