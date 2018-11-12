
#Set the minimum X value for the game
MIN_X = 0
#Set the maximum X value for the game
MAX_X = 5

#Set the maximum Y value for the game
MIN_Y = 0
#Set the maximum Y Value for the game
MAX_Y = 5

mouseX = 3
mouseY = 3

catX = 0
catY = 0

while mouseX != catX or mouseY != catY:
    print("The cat is currently at ", catX, ", ", catY)
    direction = input("Which direction do you want to go? ")
    
    #Only allow the cat to move left if it is not already at the left edge
    if direction == "l" and catX > MIN_X:
        catX = catX - 1
    #Only allow the cat to move right if it is not already at the right edge
    elif direction == "r" and catX < MAX_X:
        catX = catX + 1
    #Only allow the cat to move down if it is not already at the bottom edge
    elif direction == "d" and catY > MIN_Y:
        catY = catY - 1
    #Only allow the cat to move up if it is not already at the top edge
    elif direction == "u" and catY < MAX_Y:
        catY = catY + 1

print("You found the Mouse at ", mouseX, ",", mouseY)
