def count(book_path):
    words =book_path.split()
    num = len(words)
    return f"{num}"

def count_character(text):
    store = {}
    low = text.lower()
    for c in low:
        if c in store:
            store[c] += 1
        else:
            store[c] = 1
    return store

def sort_on(item):
    return item["num"]


def print_report(store, num):
    new_list = []
    for key, value in store.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    print(f"""========== BOOKBOT ==========
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ------------
    Found {num} total words
    --------- Character Count -------""")
    for item in new_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END =============")