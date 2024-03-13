def get_lower_case_alpha_list():
    # initialise an empty list
    list = []
    # filling the list with lowercase letter in alphabetical order
    alpha = 'a'
    for i in range(0, 26):
        list.append(alpha)
        alpha = chr(ord(alpha) + 1)
    return list
#
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
def count_letters(text):
    #refactoring from counting practice 
    lower_text = text.lower()
    letters = get_lower_case_alpha_list()
    counted_letters = {}
    for i in range(0,len(letters)):
        count = 0
        if not(letters[i] in counted_letters):
            for j in range(0,len(lower_text)):
                if letters[i] == lower_text[j]:
                    count += 1
            counted_letters[letters[i]] = count
    return counted_letters

#
def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    #print_book(file_contents)
    counted_letters_text = count_letters(file_contents)
    print(f"This book has {count_words(file_contents)} words. \n {len(file_contents)-1}")
    for a in counted_letters_text:
        amount = counted_letters_text[a]
        print(f"{a}: {amount}")
main()
