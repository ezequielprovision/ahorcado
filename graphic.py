import string_helpers

def draw_sprite(lives, graphic_word, used_letters):
    used_letters = string_helpers.show_used_letters(used_letters)
    picture = ""
    if lives == 7:
        picture = """
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
        picture = """
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
        picture = """
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
        picture = """
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
        picture = """
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
        picture = """
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
        picture = """
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
        picture = """
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

    return picture