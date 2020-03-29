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

###########################################################################
f = open(r"C:\Users\eromi\Documents\GitHub\proyectos\ahorcado\nombres_ahorc.txt", "r")
lista_palabras = []

for line in f:
    lista_palabras.append(line.strip("\n"))

f.close()

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