import random

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

def grafico(intentos, muestra):
    dibujo = ""
    if intentos == 7:
        dibujo = """
    ---------------
    |             |
    |           
    |           
    |            
    |            
    |            
    |
      {}""".format(muestra)

    if intentos == 6:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |           
    |            
    |            
    |            
    |
      {}""".format(muestra)
    elif intentos == 5:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            /
    |             
    |           
    |
    |
      {}""".format(muestra)

    elif intentos == 4:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             
    |           
    |
    |
      {}""".format(muestra)
 
    elif intentos == 3:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |           
    |
    |
      {}""".format(muestra)

    elif intentos == 2:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |            /
    |
    |
      {}""".format(muestra)
    elif intentos == 1:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |            / \\
    |
    |
      {}""".format(muestra)
    elif intentos == 0:
        dibujo = """
    ---------------
    |             |
    |           (X.X) AAAAAAAAHHHHHHGGGG!
    |           ======
    |            / \\
    |             |
    |            / \\
    |
      {}""".format(muestra)

    return dibujo

#########################  MENU INICIO  ####################################
battery_file = r"C:\Users\eromi\Documents\GitHub\proyectos\ahorcado\nombres_ahorc.txt"
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
        with open(battery_file, "r") as f:
            new_file = "" 
            for line in f:
                new_file += line   ### LEVANTA LAS PALABRAS DEL TXT
        with open(battery_file, "w") as f:
            writing_file = True
            while writing_file:   ### LOOP PARA AGREGAR VARIAS PALABRAS
                new_file += ("\n" + input("Escribe una palabra\n"))
                salir = input("""{} \nPara agregar otra palabra ingresa 1 
                Para volver al menú 2\n""".format(new_file))
                if salir == "2":
                    writing_file = False

            f.write(new_file) #ESCRIBE EN EL ARCHIVO TODAS LAS MODIF HECHAS EN LA VAR NEW_FILE
            
    elif menu == "3":
        with open(battery_file, "r") as f:
            for line in f:
                print(line.strip("\n"))

    else:
        exit()

########################### COMIENZA EL JUEGO ###########################################
play = True
score = 0
_continue = None
loaded_file = r"C:\Users\eromi\Documents\GitHub\proyectos\ahorcado\saved_scores.txt"
table_score = load_state(loaded_file) # me va a devolver un dicc con los nombres y puntajes
print('Puntajes anteriores: \n{}'.format(table_score))


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
                print(grafico(intentos, quest)) #recibe el arg quest para mostrarlo en el grafico
                intentos = intentos * 35  #Al arriesgar da un puntaje mucho mayor
                print("Sumas {} puntos!!".format(intentos))
                score += intentos #el valor de intentos ya fue multiplicado
                intentos = 0
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)".format(score))
                if _continue == "n":  ## Al ingresar 'y' va a emplezar de nuevo
                    play = False


            else:
                print("Noooo")
                intentos = 0
                print(grafico(intentos, quest))
                print("Looser!")
                if score > 0 :
                    print("Tienes un total de {} puntos".format(score))
                _continue = input("Tu puntaje es {}! \n Sigues jugando? (y = SI / n = NO)".format(score))

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
                print(grafico(intentos, muestra))
                print("Sii!, Ganaste!!")
                intentos = intentos * 10
                print("Sumas {} puntos!".format(intentos))
                score += intentos
                _continue = input("Tu puntaje TOTAL es {}! \n Sigues jugando? (y = SI / n = NO)".format(score))
                intentos = 0
                if _continue == "n":
                    play = False

            else:  ### si todavia tiene '.' 
                aux__ = no_se_que_func_tiene_python_para_esto(lista_letras_usadas)
                print("LETRAS YA USADAS: {}".format(aux__))
                print(grafico(intentos, muestra))
                
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

with open(loaded_file, "w") as f:
    f.write(to_save)

#convertir esto en print tabla con valores de mayor a menor
print(to_save)

