def bubble_sort(array):
    count = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            count += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
                
    return array

array = [1, 5, 4, 3, 7, 9 , 3, 5, 6, 10 ,20, 15]
print(bubble_sort(array))