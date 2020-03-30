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

############################################################################


lista_palabras = []

with open(r"C:\Users\eromi\Documents\GitHub\proyectos\ahorcado\nombres_ahorc.txt", "r") as f:
    for line in f:
        lista_palabras.append(line.strip("\n"))


quest = random.choice(lista_palabras)
intentos = 7


muestra = quest[0] + ("." * (len(quest) - 2)) + quest[-1]

muestra = busca_indices(muestra[0], quest, muestra) 
muestra = busca_indices(muestra[-1], quest, muestra)
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
            exit()
        else:
            print("Noooo")
            intentos = 0
            print(grafico(intentos, quest))
            print("Looser!")
            exit() 
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

        exit()
    aux__ = no_se_que_func_tiene_python_para_esto(lista_letras_usadas)
    print("LETRAS YA USADAS: {}".format(aux__))
    print(grafico(intentos, muestra))
    
    if intentos > 0:
        print("Quedan {} intentos!!".format(intentos))
    else:
        print("Que en paz descanse...")
        print("La palabra era... \"{}\"".format(quest))