import sys
from stats import get_num_words, get_num_characters, get_sorted_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_list = get_sorted_list(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


def get_book_text(fpath):
    with open(fpath) as f:
        fcontents = f.read()
    return fcontents


main()
