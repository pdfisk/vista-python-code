# ---------------------------
# 01_chicklets_first_steps.py
# ---------------------------

# chicklet is a young chick just learning to walk
# in this eposide, we tell him how to walk diagonally
# across the board

# create a game board
game = board()

# create the chick
chicklet = game.create_image('chick_right', 0, 0)

# move the chick
chicklet.move_to(1,1)
chicklet.move_to(2,2)
chicklet.move_to(3,3)
chicklet.move_to(4,4)
chicklet.move_to(5,5)
chicklet.move_to(6,6)
