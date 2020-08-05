dic1={'a':100,'b':200,'c':300,'d':200,}
dic_new={}
for i in dic1:
    if dic1[i] not in dic_new.values() :
       dic_new.update({i:dic1[i]})

print(dic_new)