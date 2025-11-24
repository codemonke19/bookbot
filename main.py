from stats import count_words
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main(path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    print(f"Found {num_words} total words")
    print(char_count)

main("./books/frankenstein.txt")