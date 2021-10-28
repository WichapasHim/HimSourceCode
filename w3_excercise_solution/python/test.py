def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        if i> 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
            # found three sum
                result.append((nums[i], nums[l], nums[r]))
                
                return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(three_sum(x))





def valid_parentheses(str_paren:str)->bool:
    if len(str_paren)%2!=0:return False
    dict_paren={'{':'}',  '(':')',   '[':']'}
    if str_paren[0] not in dict_paren : return False
    check_paren=''
    right_paren=[]
    for paren in str_paren: #'()[]' paren=(
        if paren in dict_paren:
            check_paren+=paren
            right_paren.append(dict_paren[paren]) #dict[paren]=  )
        elif paren in right_paren:
            check_paren+=right_paren[-1]
            right_paren.pop()

    return check_paren==str_paren and len(right_paren)==0








