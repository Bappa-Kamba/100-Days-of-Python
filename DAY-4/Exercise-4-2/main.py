import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

test_seed = int(input("Create a seed: "))
random.seed(test_seed)

random_index = random.randint(0, len(names) - 1)

print(f"{names[random_index]} will pay the bill.")