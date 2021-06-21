using System;
using System.Text;

namespace SolutionsInCSharp{
    public class Solution46{
        public bool BackspaceCompare(string s, string t){

            string a = GetFinalString(s);
            string b = GetFinalString(t); 

            return a.Equals(b);
        }

        public string GetFinalString(string value){
            StringBuilder s = new StringBuilder();

            foreach(var a in value){
                if(a == '#'){
                    if(s.Length != 0){
                        s.Remove(s.Length - 1, 1);
                    }
                }
                else{
                    s.Append(a);
                }
            }

            return s.ToString();

        }
    }
}