def checking(a):
     if 100<=a<1000:
         return "legal"
     else:
         return "illegal"

a=int(input('enter number'))

print(checking(a))
