i=0
k=0
sumpass=0
sumfail=0
grade =input("enter grade or done")
while grade!="done" :
    grade=int(grade)
    if 60<=grade<=100:
        sumpass = sumpass + grade
        i += 1
        print("avrage passed", sumpass / i)
        grade =input("enter grade or done")
    elif 0<=grade<60:
        sumfail= sumfail + grade
        k+=1
        print("avrage failed", sumfail / k)
        grade = input("enter grade or done")
    else:
        print("invalid grade")
        grade = input("enter grade or done")
