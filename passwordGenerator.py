import random

num = ["1","4","3","5","6"]
letter_lower = ["d","s","y","r","t","o"]
letter_upper = ["P","U","G","L","E","K"]
Symbols = ["@","#","!","^","&","$"]
list = []
password = random.choice(num)+random.choice(letter_lower)+random.choice(letter_upper)+random.choice(Symbols)


print(password)
