import random
import os
names = []
num = int(input("put the number of rounds and people here\n"))
os.system("clear")
for y in range(0,num):
    usernames = input("put the usernames here\n")
    names.append(usernames)
    os.system("clear")
dice = [1,2,3,4,5,6]
for x in range (0,num):
    final=random.choice(dice)
    dice.remove(final)
    print(str(names[x])+"\t"+str(final))
