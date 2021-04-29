using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution09
    {
        public bool IsHappy(int n)
        {
            int sum = 0;
            while(sum / 10 != 0){
                int[] numArray = splitNumber(sum);
                sum = 0;

                for(int i = 0 ; i < numArray.Length ; i++){
                    sum += numArray[i] * numArray[i];
                }

            }

            return sum == 1 ? true : false;
        }

        public int[] splitNumber(int n)
        {
            int multiplier = 10;
            int[] numArray = new int[] { };
            int i = 0;
            int remaining = n;
            do
            {
                int num = remaining % multiplier;
                numArray[i] = num;
                i++;

                remaining = remaining / multiplier;

            } while (remaining / multiplier != 0);
            return numArray;
        }
    }
}