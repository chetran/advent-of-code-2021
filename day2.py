import os

data = []

posx = 0
posy = 0

with open("inputs.txt", "r") as file:
    for i in file:
        data.append(i)

for input in range(len(data)):
    if data[input][:7] == "forward":
        posx += int(data[input][8:9])
    elif data[input][:4] == "down":
        posy -= int(data[input][5:6])
    elif data[input][:2] == "up":
        posy += int(data[input][3:4])


print(posx)
print(posy)
#when submitting dont include the minus 
print(posx*posy)
