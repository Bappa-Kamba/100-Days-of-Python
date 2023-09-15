# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

my_seed = int(input("Create a seed number: "))
random.seed(my_seed)

result = random.randint(0,1)
print(result)
if result == 0:
    print("Tails.\n")
else:
    print("Heads.\n")