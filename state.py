import os

def load(score_file):
    result = []
    if os.path.exists(score_file):
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

def sort_scores(score_list):
    i = 1 #index constant value
    for ix_1, x in enumerate(score_list):  # x is an array, [1] is the int (score)
        for ix_2 , y in enumerate(score_list):
            if ix_2 == ix_1 and ix_2 < (len(score_list) - 1):
                ix_2 += 1
            if x[i] > y[i]:
                score_list[ix_1], score_list[ix_2] = score_list[ix_2], score_list[ix_1]                
    return  score_list 

