def find_all_missing_number(nums):
    set_nums = set(nums)
    ret = []
    for i in range(1, len(nums)+1):
        if i not in set(nums):
            ret.append(i)
            
    return ret

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_all_missing_number(nums))