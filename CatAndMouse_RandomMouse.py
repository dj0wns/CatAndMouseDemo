#Allows us to use the random functon to get random numbers
import random

catX = 0
catY = 0

#Set the maximum x value that the mouse can be at
WIDTH = 3
#Set the maximum y value that the mouse can be at
HEIGHT = 3

# Set the mouse's start position to a random coordinate between (0,0) and (MAX_X,MAX_Y)
mouseX = random.randint(0,WIDTH);
mouseY = random.randint(0,HEIGHT);

while not(catX == mouseX and catY == mouseY):
    print("The cat is currently at ", catX, ", ", catY)
    direction = input("Which direction do you want to go? ")
    
    if direction == "l":
        catX = catX - 1
    if direction == "r":
        catX = catX + 1
    if direction == "d":
        catY = catY - 1
    if direction == "u":
        catY = catY + 1

print("You found the Mouse at ", mouseX, ",", mouseY)

