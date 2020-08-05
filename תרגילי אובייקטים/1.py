class person:
    def __init__(self,name,age,number_of_children=0):
        self.name=name
        self.age=age
        self.number_of_children=number_of_children

    def __str__(self):
        return (self.name,self.age,self.number_of_children)

    def hasChildren(self):
        return (bool(self.number_of_children))

    def ageGroup(self):
        if 0<=self.age<=18:
            return ("child")
        if 19<= self.age <= 60:
            return ("adult")
        if 61<= self.age:
            return ("senior")


moshe=person("moshe",12)
print(moshe.__str__())
if moshe.hasChildren():
    print(f"{moshe.name} has children")
else: print('moshe doesn\'t have kids')
print(moshe.ageGroup())



