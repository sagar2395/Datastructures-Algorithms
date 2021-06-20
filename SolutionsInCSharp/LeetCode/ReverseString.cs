using System;
using System.Text;
using System.Linq;

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

        public string ReverseString2(string value){
            if(value.Length <= 1) return value;
            else return ReverseString2(value.Substring(1)) + value[0];
        }

        public string ReverseString3(string value){
            string newVal = null;
            if(value != null || value.Length == 0 || typeof(string) != value.GetType()){
                newVal = new string(value.Reverse().ToArray());
            }
            return newVal;
        }
    }
}