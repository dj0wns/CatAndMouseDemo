#Allows us to use the random functon
import random

#Set the maximum x value that the mouse can be at
MAX_X = 3
#Set the maximum y value that the mouse can be at
MAX_Y = 3

#Set mouseX to be a random number between 0 and MAX_X
mouseX = random.randint(0,WIDTH);
#Set mouseY to be a random number between 0 and MAX_Y
mouseY = random.randint(0,HEIGHT);

catX = 0
catY = 0

while mouseX != catX or mouseY != catY:
    print("The cat is currently at ", catX, ", ", catY)
    direction = input("Which direction do you want to go? ")
    
    if direction == "l":
        catX = catX - 1
    elif direction == "r":
        catX = catX + 1
    elif direction == "d":
        catY = catY - 1
    elif direction == "u":
        catY = catY + 1

print("You found the Mouse at ", mouseX, ",", mouseY)

