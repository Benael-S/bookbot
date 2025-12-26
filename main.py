from stats import get_num_words, cnt_char, dic_to_list
#import functions from stats.py 

path = "books/frankenstein.txt" 
#book path

def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        return f.read()
# takes text file path and returns its contents

def main():
    text = get_book_text(path)
    return text 
#calls the prev function and input the path, return total file contents

result_m  = main() 
# store main() contents
book_txt = str(result_m) 
# convert results to string
char_dict = cnt_char(book_txt)
#store a dict with all chars and num of apperances using cnt_char function from stats.py
char_list_ordered = dic_to_list(char_dict)
#list of dicts for each char

"""
print(f
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
{get_num_words(book_txt)}
--------- Character Count -------)#dynamic header for file name
#start the whole prog
for i in char_list_ordered:
    if i['char'].isalpha():
        print(i['char'],i['num'])
"""

print("============ BOOKBOT ============")
print(f'Analyzing book found at {path}...')
print("----------- Word Count ----------")
print(f'Found {get_num_words(book_txt)} total words')
print("--------- Character Count -------")
for i in char_list_ordered:
    if i['char'].isalpha():
        print(i['char'] + ":" + " " + str(i['num']))
print("============= END ===============")