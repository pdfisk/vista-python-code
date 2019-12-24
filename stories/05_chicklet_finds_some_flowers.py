# ---------------------------
# 05_chicklet_finds_some_flowers.py
# ---------------------------

# assign useful variables
board_size = 7
top_left_corner = [0, 0]
bottom_right_corner = [board_size - 1, board_size - 1]
delay_time = 2
short_delay_time = 1

# create a game board
game = board()

# actor locations
global chicklet_x, chicklet_y, henrietta_x, henrietta_y
chicklet_x = chicklet_y = henrietta_x = henrietta_y = 0

# create all the images for the story
chick_in_flowers = game.create_image('chick_in_flowers')
chick_left = game.create_image('chick_left')
chick_right = game.create_image('chick_right')
hen_and_chick = game.create_image('hen_and_chick')
hen_right = game.create_image('hen_right')
house_with_flowers = game.create_image('house_with_flowers')

# helper functions
def move_chicklet_to(x, y):
    global chicklet_x, chicklet_y
    chicklet.move_to(x, y)
    chicklet_x = x
    chicklet_y = y

# clear the board
game.clear()

# place the actors in their starting positions
print('Chicklet is with his mother.')
henrietta = hen_and_chick
henrietta.move_to(top_left_corner[0], top_left_corner[1])
wait(delay_time)
print('The house with flowers is at the bottom right.')
house_with_flowers.move_to(bottom_right_corner[0], bottom_right_corner[1])
wait(delay_time)

# Chicklet leaves his mother and walks to the bottom right corner
print('Chicklet sees a house in the distance.')
wait(delay_time)
print('Bye Mom. I am going to visit the house.')
henrietta = hen_right
henrietta.move_to(top_left_corner[0], top_left_corner[1])
chicklet = chick_right
for x in range(1, board_size - 1):
    move_chicklet_to(x, x)

# Chicklet wanders into the flowers
chicklet.hide()
chicklet = chick_in_flowers
chicklet.move_to(bottom_right_corner[0], bottom_right_corner[1])
print('Chicklet wanders into the flowers.')
wait(delay_time * 2)

# Chicklet returns home
chicklet = chick_left
house_with_flowers.move_to(bottom_right_corner[0], bottom_right_corner[1])
show_chicklet()
print('Time to go home.')
wait(delay_time)
for x in range(1, board_size - 1):
    x2 = board_size - x - 1
    move_chicklet_to(x2, x2)

# Chicklet is back with his mother
chicklet.hide()
henrietta = hen_and_chick
henrietta.move_to(top_left_corner[0], top_left_corner[1])
print('Hi Mom. I found some beautiful flowers at the house.')
wait(delay_time)

# End of story
print('End of story')
