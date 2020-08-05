class Student:
    def __init__(self,name=None,id=None,address=None,grade=None):
        self.name=name
        self.id=id
        self.address=address
        self.grade=grade

    def grade_pass(self):
        return self.grade>=70

Moshe=Student('mosh',21111111,'Moshav Bitsaron',77)
if Moshe.grade_pass():
    print('pass')
else:
    print('failed')