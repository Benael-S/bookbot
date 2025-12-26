def get_num_words(book_txt):
    x = 0 # word count starts at 0
    word_ls = book_txt.split()# create list of all the words in a file
    for word in word_ls:#iterate over each word and add 1 to counter for each
        x +=1 
    return x#prints total words in file  

def cnt_char(book_txt):
    book_txt = book_txt.lower()# all text lower case for no dups
    char_count = {} # empty char dic
    for char in book_txt:
        if char not in char_count:
            char_count[char] = 1# if char not in dic add it   
        else:
            char_count[char] += 1 #if char in dic add 1 for every apearance     
    return char_count

def dic_to_list(dict):
    def sort_on(items):
        return items["num"]
    characters = []
    for key, value in dict.items():
        dict = {"char":key, "num":value}
        characters.append(dict)
    characters.sort(reverse=True, key=sort_on)
    return characters