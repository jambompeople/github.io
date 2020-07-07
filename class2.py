arr = []
what = int(input("put the number of element here"))
for y in range(0,what):
    inp = int(input("put the element here"))
    arr.append(inp)
length = len(arr)
for x in range(2, length):
    current = arr[x]
    former = x-1
    while(former>=0 and arr[former]>current):
        arr[former] = arr[former+1]
        former = former-1
        arr[former+1] = current

for j in range(length):
    print(arr[j])
