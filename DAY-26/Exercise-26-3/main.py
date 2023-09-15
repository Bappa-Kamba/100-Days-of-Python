import os

file1 = os.path.abspath('DAY-26/Exercise-26-3/file1.txt')
file2 = os.path.abspath('DAY-26/Exercise-26-3/file2.txt')


def read_file(filename):
    with open(file=filename) as file:
        data = file.readlines()
        file_contents = [line.strip() for line in data]
    return file_contents

file1_data = read_file(file1)
file2_data = read_file(file2)

result = [int(num) for num in file1_data if num in file2_data]

# Write your code above 👆

print(result)


