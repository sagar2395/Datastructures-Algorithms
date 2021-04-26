using System;
using System.Collections.Generic;

// Given a sorted array nums, remove the duplicates in-place such that each element 
// appears only once and returns the new length.
// Do not allocate extra space for another array, you must do this by modifying
// the input array in-place with O(1) extra memory.
namespace SolutionsInCSharp{
    public class A{
        public int RemoveElement(int[] nums, int val){
            int j = 0;
            int i = 0;
            while(i + j < nums.Length){
                if(nums[i] == val){
                    j++;
                }
                nums[i] = nums[i+j];
                i++;
            }
            return nums.Length - j;
        }
    }
}