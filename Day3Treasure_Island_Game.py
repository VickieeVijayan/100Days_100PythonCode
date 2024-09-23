print('''
******************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
******************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

CR = input('You are at a cross road where you want to go ? \n    Type "Left" or "Right" ? \n')

if CR == "Left" or CR == "L" or CR == "l" or CR == "left":
    WrS = input(f"You've come to the lake. There is an island in the middle  of the lake. \n" + "Type \"Wait\" to wait for a boat. Type \"Swim to swim across. \n" )
    if WrS == "Wait" or WrS == "W" or WrS == "wait" or WrS == "w":
        Door = input("You arrived at the island unharmed. There is a house with 3 doors. \n one red, one yellow, and one blue. Which colour do you choose? \n")
        if Door == "Y" or Door == "y" or Door == "Yellow" or Door == "yellow":
            print("You found the treasure! You Win!!!")
        elif Door == "R" or Door == "r" or Door == "Red" or Door == "red":
            print("It's a room full of fire. Game Over")
        elif Door == "B" or Door == "b" or Door == "Blue" or Door == "blue":
            print("You enter a room of beasts. Game Over")
        else:
            print("You have chosen option that doesn't exist. Game Over")
    elif WrS == "Swim" or WrS == "swim" or WrS == "s" or WrS == "S":
        print("You get attacked by an angry trout. Game Over")
    else:
        print("You have chosen option that doesn't exist. Game Over")
elif CR == "Right" or CR == "R" or CR == "right" or CR == "r":
    print(" You fell into a hole. Game Over")
else:
    print(f" You chosen option {CR} that doesn't exist. Game Over")


