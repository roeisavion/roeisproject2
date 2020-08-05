def gadol(list1):
    big=0
    for i in list1:
        if int(i)>int(big):
            big=int(i)
    return big
list1=input('enter list').split()
print(gadol(list1))