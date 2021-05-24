using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution09
    {
        public bool IsHappy(int n)
        {
            int sum = n;
            HashSet<int> set = new HashSet<int>();
            bool flag = false;

            while(!flag){
                List<int> numArray = splitNumber(sum);
                
                sum = 0;

                for(int i = 0 ; i < numArray.Count ; i++){
                    sum += numArray[i] * numArray[i];
                }

                if(sum == 1) flag = true;
                
                if(!set.Contains(sum)){
                    set.Add(sum);
                }
                else{
                    flag = true;
                }
            }
             
            return sum == 1 ? true : false;
        }

        public List<int> splitNumber(int n)
        {
            int multiplier = 10;
            List<int> numList = new List<int>();
            int remaining = n;
            do
            {
                int num = remaining % multiplier;
                numList.Add(num);

                remaining = remaining / multiplier;

            } while (remaining / multiplier != 0);
            
            numList.Add(remaining);
            return numList;
        }
    }
}