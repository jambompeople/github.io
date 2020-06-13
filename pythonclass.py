class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print(self.name,self.age)

Jackson = people("Jackson", 3)
Jackson.print()
