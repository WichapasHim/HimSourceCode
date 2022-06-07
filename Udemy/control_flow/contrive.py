numbers=[1,45,32,12,60]

for number in numbers:
    if number%8==0:
        #reject the list
        print("The number are unacceptable")
        break
else:
    print("All those number are fine")