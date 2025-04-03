def count_words(book):
    count  = 0
    words = book.split()
    for w in words:
        count += 1
    return count

def count_chars(book):
    char_dict = {}
    book = book.lower()
    for c in book:
        try:
            char_dict[c] += 1
        except:
            char_dict[c] = 1
    return char_dict
