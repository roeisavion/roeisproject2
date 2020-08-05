class bus():
    def __init__(self,number_of_seats):
        self.seats=['free' for i in range(number_of_seats)]

    def getOn(self,name):
        for i in range(len(self.seats)):
            if self.seats[i]=='free':
                self.seats[i]=name
                return
        print(f'the bus is full, {name} did not get on the bus')
        return

    def getOff(self,name):
        for i in range(len(self.seats)):
            if self.seats[i]==name:
                self.seats[i]='free'
                return
        print(f'there is no {name} on the bus')
        return

    def __str__(self):
        return str(self.seats)


bus1=bus(int(input('how many seats?')))
action=int(input('1-passenger on, 2-passenger off, 0-exit'))
while action!=0:
    name1=input('enter passenger name')
    if action==1:
        bus1.getOn(name1)
    if action==2:
        bus1.getOff(name1)
    print(bus1)
    action =int(input('1-passenger on, 2-passenger off, 0-exit'))

print(bus1)
