def findMedianSortedArrays(nums1, nums2):
    arr = nums1 + nums2
    arr.sort()
    result = 0
    if(len(arr)%2 == 0):
        result = float((arr[(int(len(arr)/2))-1]+arr[int((len(arr)/2)+1)-1])/2)
    else:
        result = arr[int((len(arr)+1)/2)-1]
    return result

nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1, nums2))

