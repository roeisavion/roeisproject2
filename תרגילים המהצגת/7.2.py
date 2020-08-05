l=int(input("how long do you want your dictionary?"))
dic1={}
for i in range(l):
    dic1.update({input("key"): input("value")})
key1=input("key you want to search")
print(key1 in dic1.keys())
