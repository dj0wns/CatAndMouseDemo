########################################
##------Expansion: Random Mouse,------##
##--------Boundary Check, and---------##
##------------Hot and Cold------------##
########################################
##----Add all previous expansions-----##
##---------at the same time.----------##
########################################

import random, math

MIN_X = 0
MAX_X = 5

MIN_Y = 0
MAX_Y = 5

catX = 0
catY = 0

mouseX = random.randint(MIN_X, MAX_X);
mouseY = random.randint(MIN_Y, MAX_Y);

prev_distance = math.sqrt(math.pow(catX - mouseX, 2) + math.pow(catY - mouseY, 2))

while not(catX == mouseX and catY == mouseY):
    print("The cat is currently at ", catX, ", ", catY)
    direction = input("Which direction do you want to go? ")
    
    if direction == "l" and catX > MIN_X:
        catX = catX - 1
    if direction == "r" and catX < MAX_X:
        catX = catX + 1
    if direction == "d" and catY > MIN_Y:
        catY = catY - 1
    if direction == "u" and catY < MAX_Y:
        catY = catY + 1

    new_distance = math.sqrt(math.pow(catX - mouseX, 2) + math.pow(catY - mouseY, 2))

    if new_distance > prev_distance:
        print("Colder")
    if new_distance < prev_distance:
        print("Hotter")

    prev_distance = new_distance

print("You found the Mouse at ", mouseX, ",", mouseY)

