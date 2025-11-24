from stats import (
    count_words,
    count_characters,
    reporting
)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main(path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_report = reporting(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for n in sorted_report:
        if n["char"].isalpha():
            print(f"{n['char']}: {n['num']}")
    print("============= END ===============")

main("./books/frankenstein.txt")