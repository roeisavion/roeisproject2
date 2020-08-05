grade = []
x = 0
i = 0
grade += [int(input("enter grade"))]

while 1:
    if 0 <= grade[i] <= 100:
        i += 1
        if len(grade) == 10:
            print("average", sum(grade) / len(grade))
            break
        grade += [int(input("enter grade"))]
    else:
        for i in range(5):
            grade += [int(input("enter grade"))]
            if 0 <= grade[i] <= 100:
                break
            else:
                print("too many wrong tries")
                break
