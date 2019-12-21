# ---------------------------
# 03_chicklet_explores.py
# ---------------------------

# create a game board
game = board()

# board size is 7 x 7
size = 7

# clear the board
game.clear()

# start at top left corner which is at column 0 and row 0
print('Chicklet is with his mother at the top-left corner.')
henrietta = game.create_image('hen_and_chick', 0, 0)
wait(2)

# he leaves his mother and starts walking
print('Bye mom - I am going to explore.')
henrietta = game.create_image('hen_right', 0, 0)
chicklet = game.create_image('chick_right', 1, 0)
wait(2)

# Chicklet walks to the top right corner at column 8 and row 0
print('Chicklet walks to top-right corner.')
for col in range(1, size):
    chicklet.move_to(col, 0)

# Chicklet walks to the bottom right corner at column 8 and row 8
print('Chicklet walks to bottom-right corner.')
for row in range(1, size):
    chicklet.move_to(size - 1, row)

# Chicklet walks to the bottom left corner at column 0 and row 8
print('Chicklet walks to bottom-left corner.')
chicklet = game.create_image('chick_left', size - 1, size - 1)
for col in range(0, size):
    chicklet.move_to(size - 1 - col, size - 1)

# Chicklet walks to the top left corner at column 0 and row 0
print('Chicklet walks to top-left corner.')
for row in range(1, size - 1):
    chicklet.move_to(0, size - 1 - row)

# and Chicklet is back where he started
print('Hi mom - I am back.')
wait(2)

chicklet.hide()
henrietta = game.create_image('hen_and_chick', 0, 0)
henrietta.move_to(0, 0)
print('Chicklet is now back home with his mother.')

# end of story
wait(2)
print('End of story.')
