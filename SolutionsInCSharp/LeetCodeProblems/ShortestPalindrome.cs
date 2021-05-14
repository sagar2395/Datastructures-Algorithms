using System;
using System.Linq;

namespace SolutionsInCSharp
{
    public class Solution27
    {
        public string ShortestPalindrome(string s)
        {

            int sLength = s.Length;
            if (sLength == 0) return s;
            string reversedString = new String(s.Reverse().ToArray());// reverse string using linq
                                                                      // Use separator for cases like this "aaaaa"
            string sAndReverse = s + "#" + reversedString;

            int combineStringLen = sAndReverse.Length;

            // get KMP table for the suffix
            var kmpTable = KMPPartialTable(sAndReverse);
            string reminderSubstr = reversedString.Substring(0, sLength - kmpTable[combineStringLen - 1]);
            return reminderSubstr + s;

        }




        public int[] KMPPartialTable(string sAndR)
        {
            int len = sAndR.Length;
            int[] table = new int[len];

            int j = 0;
            int i = 1; // i = 0 is always 0 so start at i = 1. also default values for the table are 0s
            while (i < len)
            {
                // 3 scenarios when they match, when the dont match and j = 0, and when they dont match and j !=0
                if (sAndR[i] == sAndR[j])
                {
                    j++;
                    table[i] = j;
                    i++;
                }
                else
                {

                    if (j != 0)
                    {
                        // reset j to value in table where j -1
                        j = table[j - 1];
                    }
                    else
                    {
                        // j = 0 and does not match
                        // just increment i
                        i++;
                    }

                }
            }

            return table;
        }
    }
}