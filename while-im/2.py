age=int(input("age "))
while 0<=age<=120 :
    if 0<=age<=18:
        print("child")
    elif 19<=age<=60 :
        print("adult")
    elif 60<=age<=120 :
        print("senior")
    else: print("error")
    age = int(input("age"))