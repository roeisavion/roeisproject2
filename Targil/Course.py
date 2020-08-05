from Targil.Student import *
class Course():
    def __init__(self,course_name,course_number):
        self.course_name=course_name
        self.course_number=course_number
        self.subjects={}
        self.student_list=[]
        self.max_students=0

    def add_student(self,name,id):
        if len(self.student_list)<self.max_students:
            self.student_list.append(Student(name,id))
            return True
        else: return False

    def add_factor(self,subject,factor):
        for i in self.student_list:
            i.calc_factor(subject,factor)

    def del_student(self,id):
        del self.student_list[id]

    def calc_avg(self):
        a=0
        for i in range (len(self.student_list)):
           a+=self.student_list[i].average()
        return a/len(self.student_list)

    def __repr__ (self):
        return f'{self.course_name} course, number {self.course_number} \nteachers: {self.subjects.values()} \n{self.student_list.__repr__()}'

# printed_student_list=[i.__str__() for i in self.student_list]