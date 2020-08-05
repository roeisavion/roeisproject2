from random import randint
x=[randint(0,9) for i in range(4)]
y=[]
z=['a','a','a','a']
print(x)
guess=int(input("enter your guess"))
for i in range (4):
    if guess==0:
        y.insert(0,0)
        z[i]="false"
    else:
        y.insert(0,guess%10)
        z[i]="false"
        guess=guess//10
print(y)

while x!=y :
    bools=0
    hits=0
    for i in range(4):
        if y[i]==x[i]:
            hits+=1
            z[i]="true"
        if y[i] in x and  y[i]!=x[i] and z[i]=="false" :
            bools+=1
            z[i] = "true"

    print("bools: ", bools)
    print("hits: ", hits)
    y=[]
    guess = int(input("enter your guess"))
    for i in range(4):
        if guess == 0:
            y.insert(0, 0)
            z[i] = "false"
        else:
            y.insert(0, guess % 10)
            guess = guess // 10
            z[i] = "false"
    print(y)
print("correct!")