x = int(input("put the number here"))
y = []
for i in range(0,x):
    z = int(input("put element here"))
    y.append(z)
print(y)
sum = 0
for q in range(0,x):
    sum = y[q]+sum
print(sum)

for j in range(2,x):
    key = y[j]
    h = j-1
    while(h>0 and y[h]>key):
        y[h+1] = y[h]
        h = h-1
        y[h+1] = key
print(y)
