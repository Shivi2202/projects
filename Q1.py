import random
print('Welcome in the game')
print('what is your name?')
name=input('enter your name:')
print('good luck',name)
words=['navgurukul','friends','education','learning']
word=random.choice(words)
print('Guess the character')
guess=input('guess a character = ')
guesses=''
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in words:
            print(char)
        else :
            print('_')
        failed+=1
    if failed==0:
        print('you win')
        print('the word is',word)
        break
    # guess=input('guess a character = ')
    if guess not in word:
        turns-=1
        print('wrong')
        print('you have',+turns,'more guess')
        if turns==0:
            print('you loss!!')