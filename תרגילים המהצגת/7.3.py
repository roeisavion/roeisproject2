dic1={'a':100,'b':200,'c':300}
dic_new={}
for i in dic1:
    print(i)
    dic_new[dic1[i]]=i
print(dic_new)
    # dic_new.update({dic1[dic1.keys()[i]]:dic1.keys()[i]})
