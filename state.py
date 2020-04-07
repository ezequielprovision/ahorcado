import os

def load(load_file):
    result = {}
    with open(load_file, 'r') as f:
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
        table_score = load(loaded_file) # me va a devolver un dicc con los nombres y puntajes
        print('Puntajes anteriores: \n{}'.format(table_score))
