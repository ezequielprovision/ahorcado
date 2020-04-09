import os

def load(score_file):
    result = []
    aux = []
    with open(score_file, 'r') as f:
        for line in f:
            line.strip("\n")
            name, score = line.split(' ') # Creates name and score
            score = int(score)            # Converts score to int
            aux.append(name)              # Inserts name
            aux.append(score)             # inserts score
            result.append(aux)            # Inserts list in lista (result)
            aux = []                      # Empty list to continue for loop
        return result


################## Funcion para diccionario #####################
#
# La dejo por si cambio de opinion
#
def _load(score_file):
    result = {}
    with open(score_file, 'r') as f:
        for line in f:
            line.strip("\n")
            key, value = line.split(' ')
            result[key] = int(value.strip('\n')) ## Saca salto de linea, y convierte en entero
        return result

##########################################################

def save(score):
    gamer_name = input("Ingresa tu nombre sin espacios en el medio \n")
    score = str(score)
    text_will_save = gamer_name + ' ' + score + '\n'
    return text_will_save


########################################################

def score_printer(loaded_file, path):
    if not os.path.exists(loaded_file):  
        with open(loaded_file, 'w') as f: 
            f.write('')
    else:
        table_score = load(loaded_file) 
        print('Puntajes anteriores: \n{}'.format(table_score))
