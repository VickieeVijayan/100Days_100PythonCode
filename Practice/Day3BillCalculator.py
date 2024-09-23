print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

bill = 0

if size == "S":
    bill += 15
    print("You have selected Small size pizza")
elif size == "M":
    bill += 20
    print("You have selected Medium size pizza")
elif size == "L":
    bill += 25
    print("You have selected Large size pizza")
else:
    print("Sorry you have given a wrong input!!")
    exit()
    #print(" Kindly select the size from the given, It is CaseSensitive S, M or L: ")
    # size = input("What size pizza do you want? S, M or L: ")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        print(f"Adding $2 to your existing bill amount ${bill}")
        bill += 2
    else:
        print(f"Adding $3 to your existing bill amount ${bill}")
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese =="Y":
    print(f"Adding $1 to your existing bill amount $${bill}")
    bill += 1
print(f"Your final bill is: ${bill}")
