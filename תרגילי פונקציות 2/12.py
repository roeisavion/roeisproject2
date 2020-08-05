from random import randint
def list_creator(n):
    list1=[]
    for i in range (n):
        list1.append(str(randint(10,1000)))
    return list1
def hafuch(num):
    return num[::-1]
def upsidedown_list_creator(list1):
    list2=[]
    for i in range(len(list1)):
        list2.append(hafuch(list1[i]))
    return list2

n=int(input('enter n'))
list1=list_creator(n)
print(list1)
print(upsidedown_list_creator(list1))
