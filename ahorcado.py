import random
###############################################################
def busca_indices(letra, quest):
    y = []
    for index, x in enumerate(quest):  # genera en index el indice, y en x el objeto dentro de quest
        if x == letra:
            y.append(index)

    return y

def match_viewer(indices, quest, muestra, letra):
    position = quest.index(letra)
    muestra = list(muestra)
    muestra[position] = letra
    muestra = "".join(muestra)
    return muestra
################################################################
intentos = 7

lista_palabras = ["pablo", "viru", "otorrinolaringologo", "roquefort", "helicoptero", "cualquiera"]

quest = random.choice(lista_palabras)
muestra = quest[0] + ("." * (len(quest) - 2)) + quest[-1]

print("Bienvenides al AhoArcade! \n Comencemos! \n")

print(quest)
print(muestra)


while intentos > 0:

    letra = input("ingresa una letra\n")
    indices = busca_indices(letra, quest)
    muestra = match_viewer(indices, quest, muestra, letra)
    print(muestra)

    intentos -= 1
    print("Quedan {} !!".format(intentos))