import random

WIDTH = 3
HEIGHT = 3

mouseX = random.randint(0,WIDTH);
mouseY = random.randint(0,HEIGHT);

catX = 0
catY = 0

while mouseX != catX or mouseY != catY:
    print "The cat is currently at ", catX, ", ", catY
    direction = raw_input("Which direction do you want to go? ")
    
    if direction == "l":
        catX = catX - 1
    elif direction == "r":
        catX = catX + 1
    elif direction == "u":
        catY = catY + 1
    elif direction == "d":
        catY = catY - 1

print "You found the Mouse at ", mouseX, ",", mouseY

