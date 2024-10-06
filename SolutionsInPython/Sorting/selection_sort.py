def selection_sort(nums):
    for i in range(len(nums)):
        smallest = nums[i]
        smallest_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < smallest:
                smallest = nums[j] 
                smallest_index = j       
        nums[i], nums[smallest_index] = nums[smallest_index], nums[i]
        
    return nums


array = [1, 5, 4, 3, 7, 9 , 3, 5, 6, 10 ,20, 15]
print(selection_sort(array))
        
    