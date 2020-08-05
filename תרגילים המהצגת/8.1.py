x={1,2,3,4,5}
y={4,5,6,7}
z=set()
z.update(x)
z.update(y)
print(z)
z.discard(4)
print(z)
print("max %d min %d average %d" %(max(z),min(z),sum(z)/len(z)))