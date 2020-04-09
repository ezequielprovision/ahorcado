import random
import os
import grafico
import menu_screen
import string_helpers
import state
    

path = os.path.abspath(__file__)  
path = os.path.dirname(path)  
battery_file = os.path.join(path, "nombres_ahorc.txt")   


path = os.path.abspath(__file__)  
path = os.path.dirname(path)  
score_file = os.path.join(path, "saved_scores.txt")

start = False

print('Bienvenides al AhoArcade:')
while not start:
    menu = input("""Elige una opción:
    1 - jugar 
    2 - agregar palabras
    3 - mostrar palabras
    4 - mostrar tabla de puntajes
    5 - borrar tabla de puntajes
    6 - salir
    """)
    if menu == "1":
        start = True

    elif menu == "2":
        menu_screen.option_2(battery_file)

    elif menu == "3":
        menu_screen.option_3(battery_file)

    elif menu == "4":
        state.score_printer(score_file, path)
    
    elif menu == "5":
        with open(score_file, "w") as f:
            pass # detele 
    else:
        exit()

########################### BEGINS THE GAME ###########################################
play = True       # Makes loop to continue playing 
score = 0         # Int of player score
_continue = None  # When 'n' play = False
words_list = []   # List of words 
hidden_word = ""  # Request word
graphic_word = "" # Will show matched letters
used_letters = [] # Stock of used letters
lives = 0         # Number of attemps befor loosing
letter = ""       # user input

with open(battery_file, "r") as f:
    for line in f:
        words_list.append(line.strip("\n"))

print("*** Comencemos! ***\n")

while play:
    hidden_word = random.choice(words_list)
    words_list.remove(hidden_word) # will not choice same word twice
    lives = 7
    used_letters = [hidden_word[0], hidden_word[-1]] 
    graphic_word = string_helpers.round_begins(graphic_word, hidden_word) # reveals 1st and last letter

    print(graphic_word)
    while lives > 0:
        letter = input("ingresa una letra, o arriesga con tu palabra definitiva\n")
        if len(letter) > 1:
            if letter == hidden_word:
                print("Acertasteee!")
                print(grafico.draw_sprite(lives, hidden_word, used_letters)) 
                lives = lives * 35  # Gambling a full word gives higher score
                print("Sumas {} puntos!!".format(lives))
                score += lives
                lives = 0
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                if _continue == "n":
                    play = False


            else:
                print("Noooo")
                lives = 0
                print(grafico.draw_sprite(lives, hidden_word, used_letters))
                print("Looser!")
                if score > 0 :
                    print("Tienes un total de {} puntos".format(score))
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                if _continue == "n":
                    play = False

        else:   ### if length = 1         
            if letter in used_letters: 
                print("Esa letra ya está utilizada, pierdes un intento!")
                lives -= 1

            else:
                used_letters.append(letter)
                aux = graphic_word
                graphic_word = string_helpers.search_matches(letter, hidden_word, graphic_word)
                graphic_word = "".join(graphic_word)

                if aux == graphic_word: # aux value is graphic_word after reveal a new letter
                    print("No!")        # If had not change, it´s wrong
                    lives -= 1
                else:                   # Else, inputed letter it´s okey
                    print("Muy bien!!")
            
            if not "." in graphic_word:
                print(grafico.draw_sprite(lives, graphic_word, used_letters))
                print("Sii!, Ganaste!!")
                lives = lives * 10
                print("Sumas {} puntos!".format(lives))
                score += lives
                _continue = input("Tu puntaje TOTAL es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                lives = 0
                if _continue == "n":
                    play = False

            else:  ### if '.' in graphic_word 
                print(grafico.draw_sprite(lives, graphic_word, used_letters))
                
                if lives > 0:
                    print("Quedan {} intentos!!".format(lives))
                else:  # lost the round
                    print("Que en paz descanse...")
                    print("La palabra era... \"{}\"".format(hidden_word))
                    if score > 0 :
                        print("Tienes un total de {} puntos".format(score))
                    _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                    if _continue == "n":
                        play = False

to_save = state.save(score)

with open(score_file, "r") as f:
    for line in f:
        to_save += line

#convertir esto en print tabla con valores de mayor a menor
print(to_save)

with open(score_file, "w") as f:
    f.write(to_save)




