###############################################################
def string_used_words(used_letters): # Crea lista de letras usadas con espacio en el medio
    result = ""
    for x in used_letters:
        result += x.upper() + " "
    return result

###############################################################
def busca_indices(letter, hidden_word, graphic_word): # Busca matches entre letter y hidden_word
    graphic_word = list(graphic_word)                # Devuelve graficword converitdo
    for index, x in enumerate(hidden_word):  # genera en index el indice, 
#                                            # y en x el objeto dentro de hidden_word
        if x == letter:
            graphic_word[index] = letter
    return graphic_word
################################################################

def convierte_string(graphic_word):   #convierte en str a graphic word, ya q se convierte en lista antes
    graphic_word = list(graphic_word)
    graphic_word[0] = graphic_word[0].upper()
    graphic_word[-1] = graphic_word[-1].upper()
    return "".join(graphic_word)
###########################################################

def round_begins(graphic_word, hidden_word): # crea grafic_word con '.' en el medio 
    graphic_word = hidden_word[0] + ("." * (len(hidden_word) - 2)) + hidden_word[-1]
    graphic_word = busca_indices(graphic_word[0], hidden_word, graphic_word) 
    graphic_word = busca_indices(graphic_word[-1], hidden_word, graphic_word)
    return graphic_word                      # no era funcion porque al princio solo se jugaba una vuelta
