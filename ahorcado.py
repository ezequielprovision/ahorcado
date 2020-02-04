import random

print("Bienvenides al AhoArcade! \n Comencemos! \n")

lista_palabras = ["pablo", "viru", "otorrinolaringologo", "roquefort", "helicoptero", "cualquiera"]

quest = random.choice(lista_palabras)

muestra = quest[0] + ("." * (len(quest) - 2)) + quest[-1]

print(quest)
print(muestra)