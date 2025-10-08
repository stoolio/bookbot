from stats import count_words, count_characters, sort_char_count
import sys;

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_count = count_characters(book_text)
    sorted_chars = sort_char_count(char_count)
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["name"].isalpha():
            print(f"{entry["name"]}: {entry["num"]}")

main()
