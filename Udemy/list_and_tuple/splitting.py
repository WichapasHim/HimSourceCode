panagram="""The quick brown
fox jumps\tover the lazy dog"""

words=panagram.split()

print(words)

number_string='9,223,372,036,854,775,807'
number_string=number_string.split(',')
print(number_string)

#Him solution List comprehension
number_int=[int(num) for num in number_string ]
print(number_int)


number=[int(i) for i in input('Please enter three numbers: ').split(',')]
print(sum(number))


