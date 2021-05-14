using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution31
    {
        public bool ContainsNearbyDuplicate(int[] nums, int k)
        {
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j <= k + i && j < nums.Length; j++)
                {
                    if (nums[i] == nums[j]) return true;
                }
            }
            return false;
        }
    }
}