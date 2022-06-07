number=input('Please enter number : ')
seperators=''
for char in number:
    if not char.isnumeric():
        seperators+=char
#print(seperators)

values="".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))

