using System;

namespace SolutionsInCSharp
{
    public class Solution04
    {
        public int MaxSubArray(int[] nums)
        {
            if(nums == null || nums.Length == 0) return 0;

            var localMax = nums[0];
            var globalMax = nums[0];
            for(int i= 0 ; i < nums.Length ; i++)
            {
                localMax = findMax(nums[i] , nums[i] + localMax);
                globalMax = findMax(localMax , globalMax);
            }

            return globalMax;
        }

        public int findMax(int a ,int b){
            return a >= b ? a : b;
        }
    }
}