def sorted_array_square(nums):
    sq_list = [num ** 2 for num in nums]
    sq_list.sort()
    return sq_list


def sorted_array_square_1(nums):

    if not nums:
        print("condition is true")
        return nums
    
    if nums[0] > 0:
        return [num ** 2 for num in nums]
    
    # Splitting array into two
    positive_index = 0
    for i, num in enumerate(nums):
        if num >= 0:
            positive_index = i
            break
        
    arr1 = nums[positive_index-1::-1]
    arr2 = nums[positive_index:]
    
    # Squaring both arrays
    arr1 = [num ** 2 for num in arr1]
    arr2 = [num ** 2 for num in arr2]
        
    # Merging and sorting both arrays
    arr = arr1 + arr2
    arr.sort()
    
    return arr
    
    
arr = [-5, -3, -1, 2, 5, 7, 9, 12]
print("hello world")
print(sorted_array_square_1(arr))
    
    