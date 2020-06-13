import datetime
import re
import math
def greeting(name):
    print("hello", name)
greeting("Jackson Ding")
print(datetime.datetime.now())
print(math.sqrt(64))
txt = "hello my name is Jackson"
x = re.search("^hello.*Jackson$",txt)
if x:
    print("sup Jackson!")
try:
    print(x)
except:
    print("there is an exception")
y = 300
def haha():
    global y
    y = 200
print(y)
haha()
print(y)
