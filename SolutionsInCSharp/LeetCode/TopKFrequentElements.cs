using System.Collections.Generic;
using System.Linq;


namespace SolutionsInCSharp{
    public class Solution10{
        public int[] TopKFrequent(int[] nums, int k){

            Dictionary<int , int> dict= new Dictionary<int, int>();

            for(int i = 0; i < nums.Length ; i++){
                if(!dict.ContainsKey(nums[i])){
                    dict[nums[i]] = 1;
                }
                else{
                    dict[nums[i]] += 1;
                }
            }

            var selected = dict.OrderByDescending(x => x.Value).Take(k);
            int[] elements = new int[k];
            int j =0;
            foreach(var element in selected){
                elements[j] = element.Key;
                j++;
            }

            return elements;
        }
    }
}