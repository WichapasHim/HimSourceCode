import random

highest=10
answer=random.randint(1,highest)
#print(answer) #TODO:Remove after testing
print("Please guess number between 1 and {} : ".format(highest))
guess=0
while True:
    guess=int(input())
    if guess==0:
        print('Quit game')
        break

    if guess==answer:
        print('Correct')
        break
    else:
        if guess<answer:
            print('please guess higher')
            
        else:
            print('Please guess lower')
            
       
    
   




"""if guess<answer:
    print('Too low')
    guess=int(input())
    if guess==answer:
        print('Well done you guessed it')
    else:
        print('Sorry, wrong')
elif guess>answer:
    print('Too high')
    guess=int(input())
    if guess==answer:
        print('Well done you guessed it')
    else:
        print('Sorry, Wrong')
else :
    print("That's correct")"""