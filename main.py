import sys
from stats import no_of_words, no_of_characters, chars_dict_to_sorted_items

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = no_of_words(text)
    chars_dict = no_of_characters(text)
    char_sorted_list = chars_dict_to_sorted_items(chars_dict)
    print_report(book_path, num_words, char_sorted_list)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()