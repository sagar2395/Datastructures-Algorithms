using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution07
    {
        public int SingleNumber(int[] nums)
        {
            HashSet<int> set = new HashSet<int>();
            int value = 0;
            for (int i = 0; i < nums.Length; i++)
            {
                if (set.Contains(nums[i]))
                {
                    set.Remove(nums[i]);
                }
                else
                {
                    set.Add(nums[i]);
                }
            }

            foreach(var val in set){
                value = val;
            }

            return value;
        }
    }
}