using System;
using System.Text;

namespace SolutionsInCSharp
{
    public class Solution45
    {
        public string ReverseString(string value){
            StringBuilder a = new StringBuilder();

            for(int i = value.Length - 1 ; i >= 0 ; i--){
                a.Append(value[i]);
            }

            return a.ToString();
        }
    }
}