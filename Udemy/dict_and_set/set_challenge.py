vowel=frozenset('aeiou')
test_text='Python is a very powerful langauge'
final_set=set(test_text).difference(vowel)
print(final_set)

final_list=sorted(final_set)
print(final_list)
