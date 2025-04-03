def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    print(get_book_text())

main()
