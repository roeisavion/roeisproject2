def motse(num,list1):
    a=0
    for i in range(len(list1)):
        if num==list1[i]:
            a=i+1
            break
    return a
list1=input("enter list").split()
num=input('checked number')
print(motse(num,list1))