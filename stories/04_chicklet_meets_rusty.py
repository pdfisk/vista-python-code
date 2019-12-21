# ---------------------------
# 04_chicklet_meets_rusty.py
# ---------------------------

# create a game board
game = board()

# board size is 7 x 7
size = 7

# create all the images for the story
print('Creating all the story images.')
doghouse = game.create_image('doghouse')
chicklet_left = game.create_image('chick_left')
chicklet_right = game.create_image('chick_right')
henrietta_and_chicklet = game.create_image('hen_and_chick')
henrietta_right = game.create_image('hen_right')
rusty_in_doghouse = game.create_image('dog_in_doghouse')
rusty_left = game.create_image('dog_left')
rusty_right = game.create_image('dog_right')

# clear the board
game.clear()

# place the actors in their starting positions
print('Chicklet is with his mother.')
henrietta = henrietta_and_chicklet
henrietta.move_to(0, 0)
wait(2)
print('Rusty is in his doghouse.')
rusty = rusty_in_doghouse
rusty.hide()
rusty.move_to(size - 1, 0)
rusty.show()
wait(2)

# Chicklet leaves his mother and starts walking
print('Bye mom - I am going to meet our neighbour.')
henrietta = henrietta_right
chicklet = chicklet_right
henrietta.move_to(0, 0)
chicklet.move_to(1, 0)
wait(2)

# Chicklet walks to the doghouse
for col in range(2, size - 2):
    chicklet.move_to(col, 0)

# Rusty comes out of his doghouse to meet Chicklet
rusty = rusty_left
doghouse.move_to(size - 1, 0)
rusty.move_to(size - 2, 0)

# They talk
print('Hello neighbour, my name is Chicklet.')
wait(2)
print('Hello Chicklet, my name is Rusty.')
wait(2)
print('Good to meet you Rusty.')
wait(2)
print('Feel free to visit any time, Chicklet.')
wait(2)
print('Goodbye Rusty.')
wait(2)
print('Goodbye Chicklet.')
wait(2)

# Rusty returns to his doghouse
print('Rusty returns to his doghouse.')
rusty.hide()
rusty = rusty_in_doghouse
rusty.move_to(size - 1, 0)
wait(2)

# Chicklet walks back to his mother
print('Chicklet walks back to his mother.')
chicklet = chicklet_left
for col in range(1, size - 2):
    chicklet.move_to(size - 2 - col, 0)

# and Chicklet is back where he started
print('Hi mom - I am back.')
wait(2)

chicklet.hide()
henrietta = game.create_image('hen_and_chick')
henrietta.move_to(0, 0)
print('Chicklet is now back home with his mother.')

# end of story
wait(2)
print('End of story.')
