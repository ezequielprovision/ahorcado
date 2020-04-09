def show_used_letters(used_letters):
    """
    Converts list to str and concatenates ' '
    """ 
    result = ""
    for x in used_letters:
        result += x.upper() + " "
    return result

###########################################################

def search_matches(letter, hidden_word, graphic_word): 
    """
    Searches letter matches in hidden word
    Returns graphic_word updated  
    """
    
    graphic_word = list(graphic_word)                
    for index, x in enumerate(hidden_word):  
        if x == letter:
            graphic_word[index] = letter
    return graphic_word

################################################################

def round_begins(graphic_word, hidden_word):
    """
    Makes graphic_word: reveals 1st and last letters, fullfits string with '.'
    """ 
    graphic_word = hidden_word[0] + ("." * (len(hidden_word) - 2)) + hidden_word[-1]
    graphic_word = search_matches(graphic_word[0], hidden_word, graphic_word) 
    graphic_word = search_matches(graphic_word[-1], hidden_word, graphic_word)
    graphic_word[0] = graphic_word[0].upper()
    graphic_word[-1] = graphic_word[-1].upper()
    return "".join(graphic_word) 
