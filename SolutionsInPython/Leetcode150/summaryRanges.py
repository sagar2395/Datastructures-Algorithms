class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(nums):
            temp = i
            while temp < len(nums) - 1 and nums[temp+1] - nums[temp] == 1:
                temp += 1
                
            if(nums[temp] == nums[i]):
                res.append(str(nums[temp]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[temp]))
                
            i = temp + 1
            
        return res
                
                
range = Solution()
print(range.summaryRanges([0,1,2,4,5,7]))