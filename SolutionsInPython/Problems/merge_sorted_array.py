def merge(arr1, arr2):
    new_array = []
    flag = 0
    first_array_index = second_array_index = 0
    while not (first_array_index>=len(arr1) or second_array_index>=len(arr2)):
        if arr1[first_array_index] <= arr2[second_array_index]:
            new_array.append(arr1[first_array_index])
            first_array_index += 1
        else:
            new_array.append(arr2[second_array_index])
            second_array_index += 1
            
        if(first_array_index==len(arr1)):
            flag = 1
            
    if flag == 1:
        for item in arr2[second_array_index:]:
            new_array.append(item)
    else:
        for item in arr1[second_array_index:]:
            new_array.append(item)
            
    return new_array

array1 = [1,3,5,7]
array2 = [2,4,6,8,10,12]
print(merge(array1,array2))