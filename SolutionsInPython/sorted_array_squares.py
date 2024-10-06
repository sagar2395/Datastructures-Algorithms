def sorted_array_square(nums):
    sq_list = [num ** 2 for num in nums]
    sq_list.sort()
    return sq_list


def sorted_array_square(nums):
    if not nums:
        return nums
    
    if nums[0] > 0:
        return [num ** 2 for num in nums]
    
    