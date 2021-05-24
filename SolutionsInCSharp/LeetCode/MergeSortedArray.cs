using System;

namespace SolutionsInCSharp
{
    public class Solution25
    {
        public void Merge(int[] nums1, int m, int[] nums2, int n)
        {
            Array.Copy(nums2, 0, nums1, m, n);
            Array.Sort(nums1);
        }
    }
}