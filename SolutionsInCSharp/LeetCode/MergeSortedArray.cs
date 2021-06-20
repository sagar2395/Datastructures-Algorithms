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

        public int[] MergeSortedArrays(int[] arr1, int[] arr2)
        {
            int i = 0, j = 0, k = 0;
            int[] newArr = new int[arr1.Length + arr2.Length];

            while (i < arr1.Length && j < arr2.Length)
            {
                if (arr1[i] < arr2[j])
                {
                    newArr[k] = arr1[i];
                    i++;
                }
                else
                {
                    newArr[k] = arr2[j];
                    j++;
                }
                k++;
            }

            if(i == arr1.Length){
                while(j < arr2.Length){
                    newArr[k] = arr2[j];
                    j++;
                    k++;
                }
            }
            else{
                while(i < arr1.Length){
                    newArr[k] = arr2[i];
                    i++;
                    k++;
                }
            }

            return newArr;
        }
    }
}