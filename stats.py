def count_words(book_text):
    words = book_text.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f"Found {num_words} total words")