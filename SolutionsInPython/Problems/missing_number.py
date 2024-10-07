def missing_number(nums):
    nums.sort()
    for i, v in enumerate(nums):
        
        if i != v:
            return v - 1
        
        if(v == len(nums) - 1):
            return v + 1
        
def missing_number_2(nums):
    return sum(range(len(nums)+ 1)) - sum(nums)
        
nums = [3, 0 ,1]

print(missing_number(nums))
print(missing_number_2(nums))
        