# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇


# Write your code above this row 👆

# 🚨 Don't change the code below 👇

col = int(position[0]) - 1
row = int(position[1]) - 1

map[row][col] = "X"


print(f"{row1}\n{row2}\n{row3}")
