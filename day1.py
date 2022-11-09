import os

data = []
count = 0

try:
    with open("inputs.txt" , "r") as file:
        for line in file:
            data.append(int(line))

    for index in range(len(data) - 1):
        if data[index] < data[index + 1]:
            count += 1

    print("There are {} measurements that are larger than the previous measurement.".format(count))

except FileNotFoundError:
    print("File not found!")
