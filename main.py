def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{file_contents}")
main()
