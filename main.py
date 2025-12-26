import sys
from stats import get_num_words, cnt_char, dic_to_list
# import functions from stats.py


def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        return f.read()
# takes text file path and returns its contents


def main():
    # --- argument check ---
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    # --- read book ---
    book_txt = get_book_text(path)

    # --- analysis ---
    char_dict = cnt_char(book_txt)
    char_list_ordered = dic_to_list(char_dict)

    # --- output ---
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_txt)} total words")
    print("--------- Character Count -------")

    for i in char_list_ordered:
        if i["char"].isalpha():
            print(i["char"] + ": " + str(i["num"]))

    print("============= END ===============")


main()



