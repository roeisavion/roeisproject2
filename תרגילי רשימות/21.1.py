from random import randint
answer=[]
guess=[]
for i in range(4):
    answer.append([str(randint(0,9)),True])

# answer=[[str(randint(0,9)),True] for i in range (4)]

print(answer)
guess= [[i, True] for i in list(input("Enter your guess(4 digits): "))]

# for i in range (4) :
#     guess.append([[input("Enter your guess(4 digits): "),1]])

while guess!=answer :
    hits=0
    bools=0
    for i in range (4) :
        if answer[i][0]==guess[i][0] :
            hits+=1
            answer[i][1]=0
            guess [i][1]=0
        for a in range (4) :
            if guess[i][0]==answer[a][0] and answer[a][1]==1 and guess[i][1]==1:
                bools+=1
                answer[a][1]=0
                guess[i][1] = 0
    print("hits: ", hits)
    print('bools: ',bools)
    guess = [[i, True] for i in list(input("Enter your guess(4 digits): "))]
    for i in range (4) :
        answer[i][1]=1

print("correct!")





