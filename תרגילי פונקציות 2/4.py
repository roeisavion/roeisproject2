def prime_check(num):
    for i in range(2,num//2+1):
        if num%i==0 :
            return 0

    return 1
num=int(input('enter a number'))
if prime_check(num):
    print('the number is prime')
else:
    print('the number is not prime')

