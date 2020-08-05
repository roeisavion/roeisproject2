names=['rafi','rinat','raz','roei','ron']
grades=[30,40,50,60,73]
pairs={}
for i in range(5):
    pairs.update({names[i]:grades[i]})
print(pairs)
average=sum(pairs.values())/len(pairs)
print("average is",average )
for i in pairs :
    if pairs[i] > average :
        print(i,"is above average")
