import random
intentos = 7
print("Bienvenides al AhoArcade! \n Comencemos! \n")

lista_palabras = ["pablo", "viru", "otorrinolaringologo", "roquefort", "helicoptero", "cualquiera"]

quest = random.choice(lista_palabras)

muestra = quest[0] + ("." * (len(quest) - 2)) + quest[-1]

print(quest)
print(muestra)


while intentos > 0:

    letra = input("ingresa una letra\n")
    if letra in quest:
        print("Está ubicada en {}".format(quest.index(letra) + 1))
        position = quest.index(letra)
        muestra = list(muestra)
        muestra[position] = letra
        muestra = "".join(muestra)
        print(muestra)
    
    else:
        print("nooooo")

    intentos -= 1
    print("Quedan {} !!".format(intentos))