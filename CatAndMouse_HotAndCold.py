########################################
##------Expansion: Hot and Cold-------##
########################################
##---We tell the player if they are---##
##----getting hotter or colder by-----##
##-----calculating the distance.------##
########################################

# Allows us to use square root and power functions to calculate distance
import math

catX = 0
catY = 0

mouseX = 3
mouseY = 3

# Calculate the distance between the cat and mouse using the distance formula
prev_distance = math.sqrt(math.pow(catX - mouseX, 2) + math.pow(catY - mouseY, 2))

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

    # Calculate the new distance using the distance formula
    new_distance = math.sqrt(math.pow(catX - mouseX, 2) + math.pow(catY - mouseY, 2))

    # Compare the new distance with the previous distance
    if new_distance > prev_distance:
        print("Colder")
    if new_distance < prev_distance:
        print("Hotter")

    # Before we move the cat again, let's save our new distance as the previous distance
    prev_distance = new_distance

print("You found the mouse at ", mouseX, ",", mouseY)
