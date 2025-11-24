from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main(path_to_file):
    book_text = get_book_text(path_to_file)
    count_words(book_text)

main("./books/frankenstein.txt")