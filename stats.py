def count_words(book_text):
    words = book_text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

def count_characters(book_text):
    char_count = {}
    small_text = book_text.lower()
    for char in small_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def helper(dict):
    return dict["num"]

def reporting(char_count):
    report = []
    for key in char_count:
        new_dict = {}
        new_dict["char"] = key
        value = char_count[key]
        new_dict["num"] = value
        report.append(new_dict)
    report.sort(reverse = True, key = helper)
    return report