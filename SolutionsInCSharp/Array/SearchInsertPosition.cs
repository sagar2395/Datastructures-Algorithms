using System;

namespace SolutionsInCSharp
{
    public class Solution03
    {
        public int SearchInsert(int[] nums, int target)
        {
            int index = 0;

            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i] >= target)
                {
                    index = i;
                    break;
                }
            }

            if (nums[nums.Length - 1] < target)
            {
                index = nums.Length;
            }

            return index;
        }
    }
}