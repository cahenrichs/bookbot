import sys
from stats import count, count_character, print_report




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    counting = count(text)
    character = count_character(text)
    print_report(character, counting)
   
  
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
   
main()
# results = get_book_text("/home/vboxuser/workspace/github.com/cahenrichs/bookbot/books/frankenstein.txt")