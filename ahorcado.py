import random
import os
import grafico
#################    FUNCIONES DEL MENU   ####################
def menu_option_2(battery_file):
    with open(battery_file, "r") as f:
        new_file = [] 
        for line in f:
            new_file.append(line.strip('\n'))   ### LEVANTA LAS PALABRAS DEL TXT

    while True:               ### Voy a suponer q el usuario ingresa la palabra de la manera adecuada
        new_word = input('Ingresa una palabra sin espacios ni caracteres raros\n')
        if new_word == '1':   ### Sino tendria que hacer una funcion que compare todos los
            break             ### caracteres a ver si son validos
        elif not new_word in new_file:
            new_file.append(new_word)
            print('Agregado!, Ingresa otra palabra o \"1\" para salir')
        else:
            print('Esa palabra ya está en la lista')


def menu_option_3(file):
    with open(file, "r") as f:
        for line in f:
            print(line.strip("\n"))

###############################################################
def no_se_que_func_tiene_python_para_esto(y):
    result = ""
    for x in y:
        result += x.upper() + " "
    return result

###############################################################
def busca_indices(letra, quest, muestra):
    muestra = list(muestra)
    for index, x in enumerate(quest):  # genera en index el indice, y en x el objeto dentro de quest
        if x == letra:
            muestra[index] = letra
    return muestra
################################################################

def letras_utilizadas(letra, lista):
    if letra in lista:
        return True

################################################################

def convierte_string(muestra):
    """ 
    result = ""
    aux = 0
    for x in muestra:
        if (aux == 0) or aux == (len(muestra) -1):
            x = x.upper()
        result += x
        aux += 1
    return result
    """
    muestra = list(muestra)
    muestra[0] = muestra[0].upper()
    muestra[-1] = muestra[-1].upper()
    return "".join(muestra)
###########################################################

def load_state(load_file):
    result = {}
    with open(load_file, 'r') as f:
        for line in f:
            line.strip("\n")
            key, value = line.split(' ')
            result[key] = int(value.strip('\n')) ## Saca salto de linea, y convierte en entero
        return result

##########################################################

def save_state(score):
    gamer_name = input("Ingresa tu nombre sin espacios en el medio \n")
    score = str(score)
    text_will_save = gamer_name + ' ' + score + '\n'
    return text_will_save
    
###########################################################



#########################  MENU INICIO  ####################################
#battery_file = r"C:\Users\eromi\Documents\GitHub\proyectos\ahorcado\nombres_ahorc.txt"
path = os.path.abspath(__file__)  # path entero de donde esta el archivo corriendo (en este caso ahorcado.py)
path = os.path.dirname(path)  # directorio del archivo, solo resta sumarle el nombre del archivo
battery_file = os.path.join(path, "nombres_ahorc.txt")  # usando os.path.join te aseguras 
# que agregue las barras correctas dependiendo del sistema operativo, 
# ya que en mac y linux es / en vez de \

start = False
while not start:
    menu = input("""Bienvenides al AhoArcade:
    Elige una opción:
    1 - jugar 
    2 - agregar palabras
    3 - mostrar palabras
    4 - salir
    """)
    if menu == "1":
        start = True

    elif menu == "2":
        menu_option_2(battery_file)

    elif menu == "3":
        menu_option_3(battery_file)
    else:
        exit()

########################### COMIENZA EL JUEGO ###########################################
play = True
score = 0
_continue = None
#loaded_file = r"C:\Users\eromi\Documents\GitHub\proyectos\ahorcado\saved_scores.txt"

path = os.path.abspath(__file__)  # path entero de donde esta el archivo corriendo (en este caso ahorcado.py)
path = os.path.dirname(path)  # directorio del archivo, solo resta sumarle el nombre del archivo
loaded_file = os.path.join(path, "saved_scores.txt")  # usando os.path.join te aseguras 
# que agregue las barras correctas dependiendo del sistema operativo, 
# ya que en mac y linux es / en vez de \


if not os.path.exists(loaded_file):  ## No tengo idea si lo que estoy haciendo esta bien
    with open(loaded_file, 'w') as f: ## Me lo pasaste como 'os.exists' y me tiro error
        f.write('')
else:
    table_score = load_state(loaded_file) # me va a devolver un dicc con los nombres y puntajes
    print('Puntajes anteriores: \n{}'.format(table_score))

############################################################################ 
# Problema al crear diccionario:
#  Si el nombre se repite (la clave del dicc) el valor mutable se va a pisar
#  o sea que si un mismo usuario graba más de una vez su nombre, el programa muestra como puntaje
#  el ultimo valor que está en el texto
#  ejemplo:
#   pablo : 250
#   pablo : 30
#   pablo : 105
#   en el print de puntajes va a devolver {'pablo' : 105}
#  
#   No se me ocurre como solucionarlo sin una forma cabeza
############################################################################ 



lista_palabras = []

with open(battery_file, "r") as f:
    for line in f:
        lista_palabras.append(line.strip("\n"))

while play:
    quest = random.choice(lista_palabras)
    lista_palabras.remove(quest) #Para que no vuelva a tocar la misma palabra 2 veces
    intentos = 7

    muestra = quest[0] + ("." * (len(quest) - 2)) + quest[-1]

    muestra = busca_indices(muestra[0], quest, muestra) 
    muestra = busca_indices(muestra[-1], quest, muestra)
    
    if _continue is None:  #de lo contrario va a mostrar el bienvenide cada vez q juegues
        print("Bienvenides al AhoArcade! \n*** Comencemos! ***\n")

    print(convierte_string(muestra))
    lista_letras_usadas = [muestra[0], muestra[-1]]


    while intentos > 0:
        aux = convierte_string(muestra)
        letra = input("ingresa una letra, o arriesga con tu palabra definitiva\n")
        if len(letra) > 1:
            if letra == quest:
                print("Acertasteee!")
                print(grafico.draw_sprite(intentos, quest)) #recibe el arg quest para mostrarlo en el grafico
                intentos = intentos * 35  #Al arriesgar da un puntaje mucho mayor
                print("Sumas {} puntos!!".format(intentos))
                score += intentos #el valor de intentos ya fue multiplicado
                intentos = 0
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                if _continue == "n":  ## Al ingresar 'y' va a emplezar de nuevo
                    play = False


            else:
                print("Noooo")
                intentos = 0
                print(grafico.draw_sprite(intentos, quest))
                print("Looser!")
                if score > 0 :
                    print("Tienes un total de {} puntos".format(score))
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))

                if _continue == "n":  ## Al ingresar 'y' va a emplezar de nuevo
                    play = False

        else:   ### o sea si el len es = 1         
            if letras_utilizadas(letra, lista_letras_usadas):
                print("Esa letra ya está utilizada, pierdes un intento!")
                intentos -= 1
                muestra = convierte_string(muestra)

            else:
                lista_letras_usadas.append(letra)
                muestra = busca_indices(letra, quest, muestra)
                muestra = convierte_string(muestra)

                if aux == muestra:
                    print("No!")
                    intentos -= 1
                else:
                    print("Muy bien!!")
            
            if not "." in muestra:
                print(grafico.draw_sprite(intentos, muestra))
                print("Sii!, Ganaste!!")
                intentos = intentos * 10
                print("Sumas {} puntos!".format(intentos))
                score += intentos
                _continue = input("Tu puntaje TOTAL es {}! \n Sigues jugando? (y = SI / n = NO)\n".format(score))
                intentos = 0
                if _continue == "n":
                    play = False

            else:  ### si todavia tiene '.' 
                aux__ = no_se_que_func_tiene_python_para_esto(lista_letras_usadas)
                print("LETRAS YA USADAS: {}".format(aux__))
                print(grafico.draw_sprite(intentos, muestra))
                
                if intentos > 0:
                    print("Quedan {} intentos!!".format(intentos))
                else:  ## si perdiste
                    print("Que en paz descanse...")
                    print("La palabra era... \"{}\"".format(quest))
                    if score > 0 :
                        print("Tienes un total de {} puntos".format(score))
                    _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)".format(score))
                    if _continue == "n":  ## Al ingresar 'y' va a emplezar de nuevo
                        play = False

to_save = save_state(score)

with open(loaded_file, "r") as f:
    for line in f:
        to_save += line

#convertir esto en print tabla con valores de mayor a menor
print(to_save)

with open(loaded_file, "w") as f:
    clean_table = input('Quieres borrar la tabla de puntajes?\n (y = SI / n = NO)\n')
    if clean_table == 'n':  # Caso contrario no guarda y el file queda en blanco
        f.write(to_save)




