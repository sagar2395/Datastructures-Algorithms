def count_smaller_numbers(nums):
    temp = sorted(nums)
    d = {}
    
    for i, num in enumerate(temp):
        if num not in d:
            d[num] = i
            
    ret = []
    
    for i in nums:
        ret.append(d[i])
        
    return ret
            
    

nums = [5,2,4,5,6,8,9]
print(count_smaller_numbers(nums))