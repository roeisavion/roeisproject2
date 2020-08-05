x=int(input())
ones=x%10
tens=x//10%10
hunderds=x//100
new=100*ones+10*tens+hunderds
print(new)