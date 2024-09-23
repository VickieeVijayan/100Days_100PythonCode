import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st option
RandomNum = random.randint(0, 4)
print(friends[RandomNum])

#2nd option
print(random.choice(friends))