dd=int(input("dd"))
mm=int(input("mm"))
yy=int(input("yy"))
mm_ones=mm%10
mm_tens=mm//10
yy_ones=yy%10
yy_tens=yy%100//10

print(dd,"//",mm_tens,mm_ones,"//",yy_tens,yy_ones)
