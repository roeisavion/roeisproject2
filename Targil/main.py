from Targil.Student import *
from Targil.Course import *

QA=Course('QA',5)
QA.subjects={'python':'orly' , 'testing':'michal' , 'menhood':'shmoolik'}
QA.max_students=3
i=0
while QA.add_student(f'aaa{i}',(i+1)*123) and QA.student_list[i].id!=0:
    QA.student_list[i].add_grade('python',(i+1)*10)
    QA.student_list[i].add_grade('testing',(i+1)*20)
    QA.student_list[i].add_grade('menhood',(i+1)*15)
    i+=1

print(QA)
QA.add_factor(input('enter factor subject'),int(input('enter factor')))
print(QA)
average_list=[i.average() for i in QA.student_list]
min=min(average_list)
for i in range (len(average_list)):
    if average_list[i]==min:
        del QA.student_list[i]
        i-=1

print(QA)

#
# input('enter student name')
# input('enter student id')
# input('enter python grade')
# input('enter testing grade')
# input('enter menhood grade')