using System;
using System.Collections.Generic;

// Given a sorted array nums, remove the duplicates in-place such that each element 
// appears only once and returns the new length.
// Do not allocate extra space for another array, you must do this by modifying
// the input array in-place with O(1) extra memory.
namespace SolutionsInCSharp{
    public class Solution{

        public int RemoveDuplicates(int[] nums){
            Dictionary<int,int> dict = new Dictionary<int,int>();
            List<int> list = new List<int>();
            for(int i = 0; i < nums.Length ; i++){
                if(!dict.ContainsKey(nums[i])){
                    list.Add(nums[i]);
                    dict[nums[i]] = 1;
                }
            }

            return list.Count;
        }

    }
}