import sys
from stats import get_count_words, get_count_chars, format_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    print(f"Found {get_count_words(contents)} total words")
    count_chars = get_count_chars(contents)
    print(count_chars)
    for x in format_count(count_chars):
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")

main()