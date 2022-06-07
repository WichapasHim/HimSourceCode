import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input(stdin).
    The function will continue looping , and prompting
    the user, until a valid `int` is entered.
    :param prompt:eiei
    :return: The integer that users enters
    """
    while True:
        temp=input(prompt)
        if temp.isnumeric():
            return int(temp)
        
        print('{} is not a valid number'.format(temp))




highest=1000
answer=random.randint(1,highest)
#print(answer) #TODO:Remove after testing
print("Please guess number between 1 and {} : ".format(highest))
guess=0
while True:
    guess=get_integer(": ")
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
            
       
    
   



