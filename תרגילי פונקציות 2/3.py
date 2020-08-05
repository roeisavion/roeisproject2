def first_and_last(word):
    for i in range(len(word)):
        print(word[0]+word[-1])
word=input('enter word')
first_and_last(word)