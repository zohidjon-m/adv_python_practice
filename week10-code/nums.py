
nums = [5,1,7,3,9]

max_value = max(nums)
min_value = min(nums)

sum_value = sum(nums)
average_value = sum_value/len(nums)
new_list = [x for x in nums if x>5]
string_value = [map(str,nums)]
print(string_value)
print(nums)
check = False
if "9" in string_value:
    check = True
    
print(f"max: {max_value}, min: {min_value}, sum: {sum_value}, average: {average_value}, new list: {new_list}, string: {string_value}, check:{check}")