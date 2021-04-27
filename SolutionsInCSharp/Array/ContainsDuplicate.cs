using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution06
    {
        public bool ContainsDuplicate(int[] nums)
        {
            HashSet<int> set = new HashSet<int>();
            for (int i = 0 ; i < nums.Length; i++)
            {
                if(!set.Contains(nums[i])){
                    set.Add(nums[i]);
                }
                else{
                    return true;
                }
            }

            return false;
        }
    }
}