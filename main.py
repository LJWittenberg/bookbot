def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter
#
def print_book(contents):
    print(f"{contents}")
#
def get_book_text(path):
    with open(path) as f:
        return f.read()
#
def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    print_book(file_contents)
    print(f"This book has {count_words(file_contents)} words.")
main()
