from random import randint
def magril(l,u,k):
    memutsa=[]
    if u>l:
        for i in range(k):
            memutsa.append(randint(l,u))
            print(memutsa[i])
    else:
        for i in range(k):
            memutsa.append(randint(u,l))
            print(memutsa[i])
    return sum(memutsa)/len(memutsa)
l=int(input('lower'))
u=int(input('upper'))
k=int(input('number of lottories'))
print('average is:',magril(l,u,k))
