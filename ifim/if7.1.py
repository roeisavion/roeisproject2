dd=int(input("dd"))
mm=int(input("mm"))
yy=int(input("yy"))
if dd<0 or dd>31:
    print("invalid day")


elif mm<=0 or mm>12:
    print("invalid month")

elif yy<1950 or yy>2020:
    print("invalid day")

elif mm==(2 or 4 or 6 or 9 or 11 or 12) and dd==31 :
    print("no such day in month")

elif (mm==2 and dd==30) or (mm==2 and dd==29 and not yy%4==0):
    print("no such day in month")
else:
    dd_ones=mm%10
    dd_tens=mm//10
    mm_ones=mm%10
    mm_tens=mm//10
    yy_ones=yy%10
    yy_tens=yy%100//10

    print(dd_tens,dd_ones,"//",mm_tens,mm_ones,"//",yy_tens,yy_ones)

