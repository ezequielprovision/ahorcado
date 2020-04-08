def draw_sprite(lives, graphic_word):
    dibujo = ""
    if lives == 7:
        dibujo = """
    ---------------
    |             |
    |           
    |           
    |            
    |            
    |            
    |
      {}""".format(graphic_word)

    if lives == 6:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |           
    |            
    |            
    |            
    |
      {}""".format(graphic_word)
    elif lives == 5:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            /
    |             
    |           
    |
    |
      {}""".format(graphic_word)

    elif lives == 4:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             
    |           
    |
    |
      {}""".format(graphic_word)
 
    elif lives == 3:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |           
    |
    |
      {}""".format(graphic_word)

    elif lives == 2:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |            /
    |
    |
      {}""".format(graphic_word)
    elif lives == 1:
        dibujo = """
    ---------------
    |             |
    |           (¬.¬)
    |            / \\
    |             |
    |            / \\
    |
    |
      {}""".format(graphic_word)
    elif lives == 0:
        dibujo = """
    ---------------
    |             |
    |           (X.X) AAAAAAAAHHHHHHGGGG!
    |           ======
    |            / \\
    |             |
    |            / \\
    |
      {}""".format(graphic_word)

    return dibujo