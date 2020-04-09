#################    FUNCIONES DEL MENU   ####################

def load_words(battery_file):
    with open(battery_file, "r") as f:
        new_file = [] 
        for line in f:
            new_file.append(line.strip('\n'))   
    return new_file

def option_2(battery_file):
    new_file = load_words(battery_file)
    with open(battery_file, "r") as f:
        new_file = [] 
        for line in f:
            new_file.append(line.strip('\n'))   
        new_word = input('Ingresa una palabra sin espacios ni caracteres raros\n')
        if not new_word in new_file:
            new_file.append(new_word)
        else:
            print('Esa palabra ya está en la lista')
    with open(battery_file, 'w') as f:
        for x in new_file:
            f.write(x + '\n')

def option_3(battery_file):
    print(load_words(battery_file))
