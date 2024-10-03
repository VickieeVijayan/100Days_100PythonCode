import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Game_Images = [rock, paper, scissors]
User_Choice = int(input("What do you choose? Type 0 for Rock,"
                        "1 for paper, or 2 for Scissors \n"))
if 0 < User_Choice >= 3:
    print("You have chosen number more than 2 or less than 0")
    exit()

print(Game_Images[User_Choice])

Comp_Choice = random.randint(0, 2)
print(f"Computer Choice: \n {Game_Images[Comp_Choice]}")
if User_Choice == 0 and Comp_Choice == 2:
    print("You Win")
elif Comp_Choice == 0 and User_Choice ==2:
    print("You loss")
elif Comp_Choice > User_Choice:
    print("You loss")
elif User_Choice > Comp_Choice:
    print("You Win")
elif User_Choice == Comp_Choice:
    print("It's Draw")

# if User_Choice == 0 and Comp_Choice == 2:
#     print(rock)
#     print(f"Computer Choice: Scissors \n {scissors}")
#     print("\n You Win")
# elif User_Choice == 1 and Comp_Choice ==0:
#     print(paper)
#     print(f"Computer Choice: Rock \n {rock}")
#     print("\n You Win")
# elif User_Choice == 2 and Comp_Choice ==1:
#     print(scissors)
#     print(f"Computer Choice: Paper \n {paper}")
#     print("\n You Win")
# elif User_Choice == 1 and Comp_Choice == 2:
#     print(paper)
#     print(f"Computer Choice: Scissors \n {scissors}")
#     print("\n You Loss")
# elif User_Choice == 0 and Comp_Choice == 1:
#     print(rock)
#     print(f"Computer Choice: Paper \n {paper}")
#     print("\n You loss")
# elif User_Choice == 2 and Comp_Choice == 0:
#     print(scissors)
#     print(f"Computer Choice: Rock \n {rock}")
#     print("\n You Loss")

