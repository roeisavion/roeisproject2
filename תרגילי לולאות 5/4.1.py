grade=[]
new_grade=0
for i in range (10) :
    new_grade=int(input("enter grade"))
    for x in range (5):
        if 0 <= new_grade <= 100:
            grade+=[new_grade]
            break
        print(x+1,"wrong tries")
        new_grade = int(input("enter grade: "))
    else:
        print("too many wrong tries")
        break
else: print("average", sum(grade) / len(grade))
