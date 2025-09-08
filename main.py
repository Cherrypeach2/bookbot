import sys
from stats import (
    get_num_words,
    get_chars_dict,
    get_sorted_char_list
)

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()
    

def main():
    book_path = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)   
    sorted_char_list = get_sorted_char_list(chars_dict)     
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")  
    print("============= END ===============")

main()