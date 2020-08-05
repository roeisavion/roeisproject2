dd=int(input("dd"))
mm=int(input("mm"))
yy=int(input("yy"))
if 0<=dd<=31 and 1<=mm<=12 and 1950<=yy<=2020  :
    dd_ones=mm%10
    dd_tens=mm//10
    mm_ones=mm%10
    mm_tens=mm//10
    yy_ones=yy%10
    yy_tens=yy%100//10

    print(dd_tens,dd_ones,"//",mm_tens,mm_ones,"//",yy_tens,yy_ones)
else: print("error")
