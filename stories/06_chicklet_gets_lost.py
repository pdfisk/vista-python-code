# ---------------------------
# 06_chicklet_get_lost.py
# ---------------------------

# assign useful variables
board_size = 7
top_left_corner = [0, 0]
top_right_corner = [board_size - 1, 0]
bottom_right_corner = [board_size - 1, board_size - 1]
delay_time = 2
short_delay_time = 1
long_delay_time = delay_time * 2

# create a game board
game = board()

# actor locations
global chicklet_x, chicklet_y, henrietta_x, henrietta_y, rusty_x, rusty_y
chicklet_x = chicklet_y = henrietta_x = henrietta_y = 0
rusty_x = board_size - 1
rusty_y = 0

# create all the images for the story
chick_in_flowers = game.create_image('chick_in_flowers')
chick_left = game.create_image('chick_left')
chick_right = game.create_image('chick_right')
doghouse = game.create_image('doghouse')
dog_in_doghouse = game.create_image('dog_in_doghouse')
dog_left = game.create_image('dog_left')
dog_right = game.create_image('dog_right')
hen_and_chick = game.create_image('hen_and_chick')
hen_left = game.create_image('hen_left')
hen_right = game.create_image('hen_right')
house_with_flowers = game.create_image('house_with_flowers')

# helper functions
def move_chicklet_to(x, y):
    global chicklet_x, chicklet_y
    chicklet.move_to(x, y)
    chicklet_x = x
    chicklet_y = y

def move_chicklet_by(x, y):
    global chicklet_x, chicklet_y
    move_chicklet_to(chicklet_x + x, chicklet_y + y)

def move_chicklet_down_right(n):
    for i in range(n):
        move_chicklet_by(1, 1)

def move_chicklet_up_left(n):
    for i in range(n):
        move_chicklet_by(-1, -1)

def move_henrietta_to(x, y):
    global henrietta_x, henrietta_y
    henrietta.move_to(x, y)
    henrietta_x = x
    henrietta_y = y

def move_henrietta_by(x, y):
    global henrietta_x, henrietta_y
    move_henrietta_to(henrietta_x + x, henrietta_y + y)

def move_henrietta_right(n):
    for i in range(n):
        move_henrietta_by(1, 0)

def move_henrietta_left(n):
    for i in range(n):
        move_henrietta_by(-1, 0)

def move_rusty_to(x, y):
    global rusty_x, rusty_y
    rusty.move_to(x, y)
    rusty_x = x
    rusty_y = y

def move_rusty_by(x, y):
    global rusty_x, rusty_y
    move_rusty_to(rusty_x + x, rusty_y + y)

def move_rusty_right(n):
    for i in range(n):
        move_rusty_by(1, 0)

def move_rusty_left(n):
    for i in range(n):
        move_rusty_by(-1, 0)

def move_rusty_up(n):
    for i in range(n):
        move_rusty_by(0, -1)

def move_rusty_down(n):
    for i in range(n):
        move_rusty_by(0, 1)

def move_rusty_and_chicklet_up_left(n):
    global chicklet_x
    for i in range(n):
        if chicklet_x > 1:
            move_chicklet_by(-1, -1)
        move_rusty_by(-1, -1)

def actor_says(name, text):
    print(name + ' says "' + text + '"')
    wait(delay_time * 2)

# clear the board
game.clear()

# place the actors in their starting positions
print('Chicklet leaves the house without his mother.')
chicklet = chick_right
move_chicklet_to(top_left_corner[0], top_left_corner[1])
wait(delay_time)
print('Rusty is in his doghouse.')
rusty = dog_in_doghouse
move_rusty_to(top_right_corner[0], top_right_corner[1])
wait(delay_time)
print('The house with flowers is at the bottom right.')
house_with_flowers.move_to(bottom_right_corner[0], bottom_right_corner[1])
wait(delay_time)

# Chicklet leaves his mother and walks to the bottom right corner
print('Chicklet sees the house in the distance.')
wait(delay_time)
actor_says('Chicklet', 'I am going to return to the house.')
move_chicklet_down_right(board_size - 2)

# Chicklet wanders into the flowers
chicklet.hide()
chicklet = chick_in_flowers
move_chicklet_to(bottom_right_corner[0], bottom_right_corner[1])
print('Chicklet falls asleep in the flowers.')
wait(long_delay_time)

# Henrietta looks for Chicklet
print('Henrietta looks for Chicklet.')
henrietta = hen_right
move_henrietta_to(top_left_corner[0], top_left_corner[1])
wait(long_delay_time)
actor_says('Henrietta', 'Chicklet, Chicklet where are you!')

# Henrietta walks over to see Rusty
print('Henrietta walks over to see Rusty.')
move_henrietta_right(board_size - 3)

# Rusty comes out of his doghouse to meet Henrietta
rusty = dog_left
doghouse.move_to(top_right_corner[0], top_right_corner[1])
move_rusty_to(board_size -2, 0)
wait(long_delay_time)

# Henrietta asks Rusty to find Chicklet
actor_says('Rusty', 'Hello Henrietta, how are you today?')
actor_says('Henrietta', 'Hello Rusty.')
actor_says('Henrietta', 'Chicklet has wandered off and I don\'t know where he is.')
actor_says('Rusty', 'He probably went to explore the house that he found.')
actor_says('Rusty', 'I will go and find him.')
actor_says('Henrietta', 'Thank you Rusty!')

# Henrietta returns home
print('Henrietta returns home.')
henrietta = hen_left
henrietta.move_to(top_right_corner[0] - 2, top_right_corner[1])
move_henrietta_left(board_size - 2)
henrietta = hen_right
henrietta.move_to(top_left_corner[0], top_left_corner[1])

# Rusty goes to find Chicklet
print('Rusty goes to find Chicklet.')
move_rusty_down(board_size - 2)

# Rusty talks to Chicklet
actor_says('Rusty', 'Hey Chicklet, your mother is looking for you!')
actor_says('Chicklet', 'Oh, I must have fallen asleep.')
actor_says('Rusty', 'Let\'s get you back home Chicklet.')
actor_says('Chicklet', 'Yes, let\'s go home.')

# Chicklet leaves the flowers
move_rusty_up(1)
chicklet = chick_left
house_with_flowers.move_to(bottom_right_corner[0], bottom_right_corner[1])
move_chicklet_to(board_size - 2, board_size - 2)

# Rusty and Chicklet walk together
move_rusty_and_chicklet_up_left(board_size - 3)

# They arrive home
actor_says('Rusty', 'Hi Henrietta, I found Chicklet.')
actor_says('Henrietta', 'Thank you Rusty!')
actor_says('Henrietta', 'Welcome home Chicklet!')

# Chicklet is now home with Henrietta
chicklet.hide()
chicklet = hen_and_chick
move_chicklet_to(top_left_corner[0], top_left_corner[1])

# They say goodbye
actor_says('Rusty', 'I will go home now.')
actor_says('Henrietta', 'Thanks again Rusty!')
actor_says('Chicklet', 'Thank you Rusty.')

# Rusty walks home
rusty = dog_right
move_rusty_to(top_left_corner[0] + 1, top_left_corner[1])
move_rusty_right(board_size - 3)

# Rusty enters the doghouse
rusty.hide()
rusty = dog_in_doghouse
move_rusty_to(top_right_corner[0], top_right_corner[1])
print('Rusty is home')
wait(long_delay_time)

# End of story
print('End of story')
