x=[input("enter string") for i in range(5)]
a=0
for i in range(5):
    if len(x[i])>=4 and x[i][-1]==x[i][0]:
        a+=1
print(a)