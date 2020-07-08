
arr = []
what = int(input("put the number of element here"))
for y in range(0,what):
    inp = int(input("put the element here"))
    arr.append(inp)
length = len(arr)

for z in range(1, length):
    j = z-1
    b = arr[z]
    while(b<arr[j] and j>=0):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = b
 print(sorted(arr))
