import os

def load(score_file):
    result = []
    if os.path.exists(score_file):
        with open(score_file, 'r') as f:
            for line in f:
                line.strip("\n")
                name, score = line.split(' ')
                score = int(score)
                result.append([name, score])
    return result

##########################################################

def user_data(score):
    player_data_list= []
    gamer_name = input("Ingresa tu nombre (Hasta 8 letras) \n")
    gamer_name = gamer_name[:8].replace(' ', '_')
    player_data_list.append(gamer_name)
    player_data_list.append(score)    
    return player_data_list


########################################################

def sort_scores(score_list):
    for x in range(0, len(score_list)):
        for y in range(x + 1, len(score_list)):
            a = score_list[x]
            b = score_list[y]
            if a[1] < b[1]: 
                score_list[x], score_list[y] = score_list[y], score_list[x]                
    return  score_list 

#######################################################

def save(score_list, score_file):
    save_str_format = ""
    for x in score_list:
        save_str_format += x[0] + ' ' + str(x[1]) + '\n'
    with open(score_file, 'w') as f:
        f.write(save_str_format)
