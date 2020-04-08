import random
import os
import grafico
import menu_screen
import string_helpers
import state
    

path = os.path.abspath(__file__)  # path entero de donde esta el archivo corriendo (en este caso ahorcado.py)
path = os.path.dirname(path)  # directorio del archivo, solo resta sumarle el nombre del archivo
battery_file = os.path.join(path, "nombres_ahorc.txt")  # usando os.path.join te aseguras 
# que agregue las barras correctas dependiendo del sistema operativo, 
# ya que en mac y linux es / en vez de \

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

########################### COMIENZA EL JUEGO ###########################################
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

    graphic_word = string_helpers.round_begins(graphic_word, hidden_word) # reveals 1st and last letter

    print(string_helpers.convierte_string(graphic_word))
    
    used_letters = [graphic_word[0], graphic_word[-1]]

    while lives > 0:
        aux = string_helpers.convierte_string(graphic_word)
        letter = input("ingresa una letra, o arriesga con tu palabra definitiva\n")
        if len(letter) > 1:
            if letter == hidden_word:
                print("Acertasteee!")
                print(grafico.draw_sprite(lives, hidden_word)) 
                lives = lives * 35  #Al arriesgar da un puntaje mucho mayor
                print("Sumas {} puntos!!".format(lives))
                score += lives #el valor de lives ya fue multiplicado
                lives = 0
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                if _continue == "n":  ## Al ingresar 'y' va a emplezar de nuevo
                    play = False


            else:
                print("Noooo")
                lives = 0
                print(grafico.draw_sprite(lives, hidden_word))
                print("Looser!")
                if score > 0 :
                    print("Tienes un total de {} puntos".format(score))
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))

                if _continue == "n":  ## Al ingresar 'y' va a emplezar de nuevo
                    play = False

        else:   ### o sea si el len es = 1         
            if letter in used_letters: #letras_utilizadas
                print("Esa letra ya está utilizada, pierdes un intento!")
                lives -= 1
                graphic_word = string_helpers.convierte_string(graphic_word)

            else:
                used_letters.append(letter)
                graphic_word = string_helpers.busca_indices(letter, hidden_word, graphic_word)
                graphic_word = string_helpers.convierte_string(graphic_word)

                if aux == graphic_word:
                    print("No!")
                    lives -= 1
                else:
                    print("Muy bien!!")
            
            if not "." in graphic_word:
                print(grafico.draw_sprite(lives, graphic_word))
                print("Sii!, Ganaste!!")
                lives = lives * 10
                print("Sumas {} puntos!".format(lives))
                score += lives
                _continue = input("Tu puntaje TOTAL es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                lives = 0
                if _continue == "n":
                    play = False

            else:  ### si todavia tiene '.' 
                aux__ = string_helpers.string_used_words(used_letters)
                print("LETRAS YA USADAS: {}".format(aux__))
                print(grafico.draw_sprite(lives, graphic_word))
                
                if lives > 0:
                    print("Quedan {} lives!!".format(lives))
                else:  ## si perdiste
                    print("Que en paz descanse...")
                    print("La palabra era... \"{}\"".format(hidden_word))
                    if score > 0 :
                        print("Tienes un total de {} puntos".format(score))
                    _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)".format(score))
                    if _continue == "n":  ## Al ingresar 'y' va a emplezar de nuevo
                        play = False

to_save = state.save(score)

with open(score_file, "r") as f:
    for line in f:
        to_save += line

#convertir esto en print tabla con valores de mayor a menor
print(to_save)

with open(score_file, "w") as f:
    f.write(to_save)




