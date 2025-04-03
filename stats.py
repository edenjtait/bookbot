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

def sort_on(dict):
    return dict["count"]

def sort_dict(d):
    char_list = []
    for char, count in d.items():
        char_dict = {"character": char, "count": count}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list
