def mutiply(x, y):
    result=x*y
    return result


def is_palindrome(string:str)->bool:
    return string[::-1].casefold()==string.casefold()


def palindrome_sentence_him(string):
    string=string.casefold()
    palindrome_check=''
    for letter in string:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            palindrome_check+=letter
    return is_palindrome(palindrome_check)


def palindrome_sentence_tim(sentence):
    string=''
    for char in sentence:
        if char.isalnum():
            string+=char
    return is_palindrome(string)


def sum_eo(n,t):
    if t!='e' and t!='o': return -1
    sum=0
    if t=='e':
        for i in range(0,n,2):
            sum+=i
    if t=='o':
        for i in range(1,n,2):
            sum+=i
    return sum


def fibonanci(n:int)->int:
    """
    Return the `n` Fibonanci number, for positive `n`.
    """
    if 0<=n<=1:
        return n
    n_minus1,n_minus2=1,0
    result=None
    for f in range(n-1):
        result=n_minus2+n_minus1
        n_minus2=n_minus1
        n_minus1=result
    return result

for i in range(36):
    print(i,fibonanci(i))



def test_annotation(x:int,y:int)->float:
    return x+y
print(test_annotation('him','bet'))




















#print(sum_eo(7,'aaaa'))




"""answer=mutiply(10.5,4)
print(answer)


forty_two=mutiply(6,7)
print(forty_two)

print()

for value in range(1,5):
    two_time=mutiply(value,2)
    print(two_time)"""

#word=input("Please enter a word to check: ")
"""if is_palindrome(word):
    print('{} is a plindrome'.format(word))
else:
    print('{} is not palindrome'.format(word))"""

#print('{} is a palindrome'.format(word)  if is_palindrome(word) else '{} is not palindrome'.format(word))
#print('{} is a palindrome'.format(word)  if palindrome_sentence_him(word) else '{} is not palindrome'.format(word))
#print('{} is a palindrome'.format(word)  if palindrome_sentence_tim(word) else '{} is not palindrome'.format(word))




