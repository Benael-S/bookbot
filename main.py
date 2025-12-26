from stats import get_num_words, cnt_char#import functions from stats.py 

def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        return f.read()
# takes text file path and returns its contents

def main():
    path = "/home/benael/projects/github.com/bookbot/books/frankenstein.txt"
    text = get_book_text(path)
    return text 
#calls the prev function and input the path, return total file contents

result_m  = main() # store main() contents
book_txt = str(result_m) # convert results to string


get_num_words(book_txt)#start the whole prog
cnt_char(book_txt)