import string_helpers

def draw_sprite(lives, graphic_word, used_letters):
    used_letters = string_helpers.show_used_letters(used_letters)
    dibujo = ""
    if lives == 7:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           
    |           
    |            
    |            
    |            
    |
      {}""".format(used_letters, graphic_word)

    if lives == 6:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           (¬.¬)
    |           
    |            
    |            
    |            
    |
      {}""".format(used_letters, graphic_word)
    elif lives == 5:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           (¬.¬)
    |            /
    |             
    |           
    |
    |
      {}""".format(used_letters, graphic_word)

    elif lives == 4:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             
    |           
    |
    |
      {}""".format(used_letters, graphic_word)
 
    elif lives == 3:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |           
    |
    |
      {}""".format(used_letters, graphic_word)

    elif lives == 2:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |            /
    |
    |
      {}""".format(used_letters, graphic_word)
    elif lives == 1:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |            / \\
    |
    |
      {}""".format(used_letters, graphic_word)
    elif lives == 0:
        dibujo = """
      LETRAS YA USADAS: {}
    ---------------
    |             |
    |           (X.X) AAAAAAAAHHHHHHGGGG!
    |           ======
    |            / \\
    |             |
    |            / \\
    |
      {}""".format(used_letters, graphic_word)

    return dibujo