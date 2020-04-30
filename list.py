digit = 8
numbers = [1,2,3,4,5,6,7,8,9,0]
letters = ['a','b','c','d','e']

specialCharacter = []
for x in range(3):
    if x == 1:
        for z in numbers:
            print(z)
    if x == 2:
        for y in letters:
            print(y)
print(numbers[0])
