age=int(input("age"))
if 0<=age<=18:
    print("child")
elif 19<=age<=60 :
    print("adult")
elif 60<=age<=100 :
    print("senior")
else: print("error")
