# ---------------------------
# 02_chicklet_practises_walking.py
# ---------------------------

# let's have chicklet walk diagonally across the board again
# this time, we will use loops so that we don't have
# to write as much code.

# create a game board
game = board()

# create the chick
chicklet = game.create_image('chick_right', 0, 0)

# move the chick
for x in range(1, 7):
    chicklet.move_to(x, x)
