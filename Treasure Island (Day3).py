print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

left_or_right = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")

if left_or_right == "left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")

    if swim_or_wait == "wait":
        which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")

        if which_door == "red":
            print("It's a room full of fire. Game Over.")
        elif which_door == "yellow":
            print("You found the treasure! You Win!")
        elif which_door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")