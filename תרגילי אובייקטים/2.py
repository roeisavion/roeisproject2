class circle():
    def __init__(self,radius):
        self.radius=radius
        self.PI=3.14

    def area(self):
        return self.radius * self.radius *self.PI

    def circumference(self):
        return self.radius*self.PI*2

cir1=circle(int(input('enter radius')))
print(f'area is {cir1.area()}')
print(f'circumference is {cir1.circumference()}')
