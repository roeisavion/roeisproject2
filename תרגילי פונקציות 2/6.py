def hanaha(age,city) :
    discont_prcnt=0
    if age<=10:
        discont_prcnt=100
    if 10<age<=18 :
        discont_prcnt=25
    if 10<age<=18 and city=='Jerusalem':
        discont_prcnt=35
    if 18<age<=60 and city=='Jerusalem':
        discont_prcnt=10
    if age>60:
        discont_prcnt=50
    return discont_prcnt

def caculator(full_price, discont_prcnt):
    new_price=full_price*(100-discont_prcnt)/100
    return new_price

age=int(input('age'))
city=input('city')
full_price=int(input('full price'))
print('new price is:', caculator(full_price,hanaha(age,city)))