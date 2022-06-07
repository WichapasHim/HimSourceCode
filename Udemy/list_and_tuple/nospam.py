menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

#TimSolution
for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index]=='spam':
            del meal[index]
    print(', '.join(meal))


















"""for meal in menu:
    for item in meal:
        if item!='spam':
            print(item,end=', ')
    print()

#HimSolution
test=['spam','a','b','spam']
print(test.count('spam'))


for meal in menu:
    if 'spam' not in meal:
        print(meal)
    else:
        count_spam=meal.count('spam')
        for i in range(0,count_spam):
            meal.remove('spam')
        print(meal)"""