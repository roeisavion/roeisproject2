def summing (a):
    'this function sums up 3 digits number'

    summ=a%10+a//10%10+a//100
    return (summ)

a=int(input('enter a'))



print(summing(a))