
def twoSum(nums, target):
    i = j = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i != j):
                if(target == nums[i] + nums[j]):
                    return [i, j]
                    
def twoSumsHashmap(nums, target):
    dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if(diff in dict):
            return i, dict[diff]
        else:
            dict[nums[i]] = i
    
                
                
nums = [3,2,4] 
target = 6
print(twoSumsHashmap(nums, target))