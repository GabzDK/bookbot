from stats import word_count, count_characters, sorted_report

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    path ='books/frankenstein.txt'
    text = get_book_text(path)
    chars_dict = count_characters(text)
    print(f"{word_count(text)} words found in the document")
    print(sorted_report(chars_dict))

main()
