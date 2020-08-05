def meagel(num) :
    sheerit=num-int(num)
    if sheerit>=0.5:
        return int(num)+1
    else:
        return int(num)

a=float(input('enter number a'))
b=float(input('enter number b'))
print(meagel(a))
print(meagel(b))
