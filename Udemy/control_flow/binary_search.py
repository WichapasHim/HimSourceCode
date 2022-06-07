low=1
high=1000

print("Please think of a number between {} and {}".format(low,high))

input('Press Enter to Start')

guesses=1


while low!=high:
    #print('Low is {0}  high is {1}'.format(low,high))
    guess=low+(high-low)//2
    high_low=input('My guess is {} . Should I guess high or lower Enter h or l , or c if my gues was correct '.format(guess)).casefold()
    if high_low=="h":
        #Guess higher. The low end of the ranges become 1 greater than guess
        low=guess+1
    elif high_low=='l':
        #Guess lower . The high end of the ranges become one less than the guess
        high=guess-1
    elif high_low=='c':
        print('I got it in {} guesses'.format(guesses))
        break
    else:
        print('Please enter h ,l or c')                                                                                              
    guesses+=1
else:
    print('You tough of the number {}'.format(low))
    print('I got it in {} guesses'.format(guesses))
