########################################
##-----Expansion: Boundary Check------##
########################################
##-----The cat can't move past a------##
##-----------set boundary.------------##
########################################

#Set the minimum X value for the game board
MIN_X = 0
#Set the maximum X value for the game board
MAX_X = 5

#Set the maximum Y value for the game board
MIN_Y = 0
#Set the maximum Y Value for the game board
MAX_Y = 5

catX = 0
catY = 0

mouseX = 3
mouseY = 3

while not(catX == mouseX and catY == mouseY):
    print("The cat is currently at ", catX, ", ", catY)
    direction = input("Which direction do you want to go? ")
    
    #Only allow the cat to move left if it is not already at the left edge
    if direction == "l" and catX > MIN_X:
        catX = catX - 1
    #Only allow the cat to move right if it is not already at the right edge
    if direction == "r" and catX < MAX_X:
        catX = catX + 1
    #Only allow the cat to move down if it is not already at the bottom edge
    if direction == "d" and catY > MIN_Y:
        catY = catY - 1
    #Only allow the cat to move up if it is not already at the top edge
    if direction == "u" and catY < MAX_Y:
        catY = catY + 1

print("You found the Mouse at ", mouseX, ",", mouseY)
