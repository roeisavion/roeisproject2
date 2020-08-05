password=input("enter password")
for i in range(5) :
    password1 = input("re-enter password")
    if password==password1 :
        print("log in sucsessfuly")
        break

else: print("too many tries")
