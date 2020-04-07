###############################################################
def string_used_words(lista_letras_usadas):
    result = ""
    for x in lista_letras_usadas:
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

def convierte_string(muestra):
    muestra = list(muestra)
    muestra[0] = muestra[0].upper()
    muestra[-1] = muestra[-1].upper()
    return "".join(muestra)
###########################################################