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
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{print_book(file_contents)} This book has {count_words(file_contents)} words.")
main()
