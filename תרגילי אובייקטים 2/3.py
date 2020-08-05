from random import randint
class loto():
    def __init__(self):
        self.list1=[]
        self.prize=1000000
        self.magril6()




    def magril6(self):
        self.list1=[randint(1,45) for i in range(6)]

    def prizeChange(self):
        self.prize=int(input('enter prize'))

    def __str__(self):
        return str(self.list1)

    def numCheck(self,checked_num):
        return checked_num in self.list1

    def caculation(self,num_of_correct_answers):
        if num_of_correct_answers<=1:
            return 0
        if 2<=num_of_correct_answers<=6:
            return num_of_correct_answers/6*self.prize

loto1=loto()
loto1.magril6()
print(loto1)
count=0
for i in range(6):
    guess=int(input("enter a guess betwin 1-45"))
    if 1<=guess<=45:
        count+=loto1.numCheck(guess)

    else:
        print('illigal guess')
        count=0
        break
print(loto1.caculation(count))

