def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main(path_to_file):
    book_text = get_book_text(path_to_file)
    return book_text

def count_words(path_to_file):
    text = main(path_to_file)
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f"Found {num_words} total words")

count_words("./books/frankenstein.txt")