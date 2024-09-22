print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

split = ((bill + ((tip / 100) * bill)) / people)

print(f"Each share would be ${ round(split, 2)}")