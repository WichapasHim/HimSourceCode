# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def valid_parentheses(str_paren:str)->bool:
    if len(str_paren)%2!=0:return False
    dict_paren={'{':'}','(':')','[':']'}
    if str_paren[0] not in dict_paren : return False
    check_paren=''
    right_paren=[]
    for paren in str_paren:
        if paren in dict_paren:
            check_paren+=paren
            right_paren.append(dict_paren[paren])
        elif paren in right_paren:
            check_paren+=right_paren[-1]
            right_paren.pop()

    return check_paren==str_paren and len(right_paren)==0


print(valid_parentheses('(('))
