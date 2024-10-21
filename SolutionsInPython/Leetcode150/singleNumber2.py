class Solution(object):
    
    #Hashmap
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for num in nums:
            if dict[num] != 3:
                return num
