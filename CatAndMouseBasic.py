# Set the cat's start position to (0,0)
catX = 0
catY = 0

# Set the mouse's start position to (3,3)
mouseX = 3
mouseY = 3

# The cat catches the mouse when the cat's position is the same as the mouse's position
# This happens when catX == (is equal to) mouseX AND catY == mouseY

# While the cat's position does NOT equal the mouse's position
# (meaning: while the cat has NOT caught the mouse)
while not(catX == mouseX and catY == mouseY):

    # Tell the player the current position of the cat.
    print("The cat is currently at ", catX, ", ", catY)

    # Ask the player for a direction and hold the answer in a variable
    direction = input("Which direction do you want to go? ")
    
    # If the player said "l", the cat goes left (decrease catX)
    if direction == "l":
        catX = catX - 1
    # If the player said "r", the cat goes right (increase catX)
    if direction == "r":
        catX = catX + 1
    # If the player said "d", the cat goes down (decrease catY)
    if direction == "d":
        catY = catY - 1
    # If the player said "r", the cat goes up (increase catY)
    if direction == "u":
        catY = catY + 1

# When we get outside the while loop, we know that the cat has caught the mouse
# Tell the player they won
print("You found the mouse at ", mouseX, ",", mouseY)
