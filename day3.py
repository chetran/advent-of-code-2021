import os

data = []
gamma = ""
epsilon = ""

def conBinDec(bin):
    length = len(bin)
    sum = 0
    for i in range(len(bin)):
        sum += int(bin[i]) * 2**(length - 1) #Reason for 2^(length-1) is because we go from left to right, just draw it if you dont remember!
        length -= 1
    return sum

with open("inputs.txt", "r") as file:
    for line in file:
        data.append(line)

for bit in range(len(data[0]) - 1): # Reason for data[0], they are all the same length and we have to check each bit. Basically, a binary number with 5 bits will be iterated 5 times but we're also gonna do that for all of the inputs in the next for loop.
    # We need to know which of these is the most dominant in each bit.
    one = 0
    zero = 0

    for input in range(len(data)): # Loops through a specific bit in each of the inputs
        if data[input][bit : bit + 1] == "1":
            one += 1
        else:
            zero += 1
    # Checks which is most dominant for this bit!
    if one > zero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# This is supposed to be the power consumption
print(conBinDec(gamma) * conBinDec(epsilon))


