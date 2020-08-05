def sofer(num,list1):
    a=0
    for i in list1:
        if num==i:
            a+=1
    return a
list1=input("enter list").split()
num=input('checked number')
print(sofer(num,list1))