using System;
using System.Collections.Generic;

// Given a sorted array nums, remove the duplicates in-place such that each element 
// appears only once and returns the new length.
// Do not allocate extra space for another array, you must do this by modifying
// the input array in-place with O(1) extra memory.
namespace SolutionsInCSharp{
    public class Solution02{
        public int RemoveElement(int[] nums, int val){
            if(nums.Length == 0 || nums == null) return 0;
            
            var index = 0;
            for(int i = 0; i < nums.Length ; i++){
                if(nums[i] != val){
                    nums[index] = nums[i];
                    index++;
                }
            }
            return index;
        }
    }
}