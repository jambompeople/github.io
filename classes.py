class students:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def printInfo(self):
        print(self.name, self.age, self.grade)

s1 = students("Jackson", 13, 8)
s1.printInfo()