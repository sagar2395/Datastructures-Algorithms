using System.Collections.Generic;

namespace SolutionsInCSharp{
    public class Solution40{

        public bool ContainsCommonItem(int[] arr1, int[] arr2){
            HashSet<int> set = new HashSet<int>();

            foreach(var val in arr1){
                set.Add(val);
            }

            foreach(var val in arr2){
                if(set.Contains(val))
                    return true;
            }

            return false;
        }

    }
}