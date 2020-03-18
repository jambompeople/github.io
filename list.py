myList  = ["hello","good morning","goodbye"]
num1 = 200
num2 = 201
num3 = 202

if num1>num2:
    print(myList[1])
elif num2<num3:
    print(myList[0])
    if num1<num2:
        print(myList[1])
else:
    print(myList[2])
