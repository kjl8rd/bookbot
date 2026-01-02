import sys
def get_book_text(texts):
    with open(texts) as f:
        file_contents = f.read()
    return file_contents

from stats import get_book_word_count
from stats import get_char_count
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        print ("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]} ...")
        print("----------- Word Count ----------")
        print (f"Found {get_book_word_count(text)} total words" )
        chars = get_char_count(text)
        chars = chars_dict_to_sorted_list(chars)
        print ("--------- Character Count -------")
        for i in chars:
            ch = i["char"]
            count = i["num"]
            if not ch.isalpha():
                continue
            print(f"{ch}: {count}")
main()


