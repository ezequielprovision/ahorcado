import os

def load(score_file):
    if not os.path.exists(score_file):  
        with open(score_file, 'w') as f: 
            f.write('')
        print('No hay puntajes anteriores')
    else:
        result = []
        aux = []
        with open(score_file, 'r') as f:
            for line in f:
                line.strip("\n")
                name, score = line.split(' ') # Creates name and score
                score = int(score)            # Converts score to int
                aux.append(name)              # Inserts name
                aux.append(score)             # inserts score
                result.append(aux)            # Inserts list in list (result)
                aux = []                      # Empty list to continue for loop
            return result


##########################################################

def user_data(score):
    """
    returns the sames contents as a list and as a string
    """
    player_data_list= []
    player_data_str = ''
    gamer_name = input("Ingresa tu nombre sin espacios en el medio \n")
    player_data_list.append(gamer_name)
    player_data_list.append(score)    
    score = str(score)
    player_data_str = gamer_name + ' ' + score + '\n'
    return player_data_list, player_data_str


########################################################

