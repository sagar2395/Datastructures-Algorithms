using System;
using System.Linq;

namespace SolutionsInCSharp
{
    public class Solution05
    {
        public void BruteForceRotateArray(int[] nums, int k)
        {
            for (int i = 0; i < k; i++)
            {
                int temp = nums[nums.Length - 1];

                for (int j = nums.Length - 1; j > 0; j--)
                {
                    nums[j] = nums[j - 1];
                }

                nums[0] = temp;
            }
        }

        public void RotateArray(int[] nums, int k)
        {
            int[] temp = new int[k];

             if(k > nums.Length){
                k = k % nums.Length;
            }

            temp = nums.Skip(nums.Length - k).Take(k).ToArray();

            for(int i =nums.Length -1 - k ; i >=0 ; i--){
                nums[i + k] = nums[i];
            }

            for(int i = 0; i < k ; i++){
                nums[i] = temp[i];
            }
        }
    }
}