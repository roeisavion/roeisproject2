factor=int(input("factor"))
new_grade=[]
grade=[]
for i in range (5) :
    grade+=[int(input("grade"))]
    new_grade+=[grade[i]*(1+factor/100)]
    print("new grade" , new_grade[i])

print("new average",sum(new_grade)/len(new_grade))
print("old average",sum(grade)/len(grade))
print("the diffrence is",sum(new_grade)/len(new_grade) - sum(grade)/len(grade) )