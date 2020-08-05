class Student ():
    def __init__(self,name,id):
        self.id=id
        self.grade_dict={}
        self.name=name

    def add_grade(self,subject,grade):
        self.grade_dict[subject]=int(grade)

    def __repr__(self):
        return f'student name : {self.name} id : {self.id} \ngrade list:{self.grade_dict}'

    def calc_factor(self,subject,factor):
        if self.grade_dict[subject]*(1+factor/100) <=100 :
            self.grade_dict[subject]*=(1+factor/100)

    def average(self):
        return sum(self.grade_dict.values())/len(self.grade_dict)





# moshe=Student('moshe',123)
# moshe.add_grade('math',90)
# moshe.add_grade('bio',83)
# moshe.add_grade('sport',78)
# print(moshe)
# moshe.calc_factor('bio',10)
# moshe.calc_factor('math',20)
# print(moshe)
# print(moshe.average())
