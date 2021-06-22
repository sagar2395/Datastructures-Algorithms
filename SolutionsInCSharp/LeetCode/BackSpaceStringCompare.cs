using System;
using System.Text;

namespace SolutionsInCSharp
{
    public class Solution46
    {
        public bool BackspaceCompare(string s, string t)
        {

            string a = GetFinalString(s);
            string b = GetFinalString(t);

            return a.Equals(b);
        }

        public string GetFinalString(string value)
        {
            StringBuilder s = new StringBuilder();

            foreach (var a in value)
            {
                if (a == '#')
                {
                    if (s.Length != 0)
                    {
                        s.Remove(s.Length - 1, 1);
                    }
                }
                else
                {
                    s.Append(a);
                }
            }

            return s.ToString();

        }

        public bool BackspaceCompare2(string s, string t)
        {
            int a = s.Length - 1;
            int b = t.Length - 1;
            
            while (a >= 0 || b >= 0)
            {
                if(s[a] == '#' || t[b] == '#'){
                    if(s[a] == '#'){
                        int backCount = 2;
                        while(backCount > 0 ){
                            a--;
                            backCount--;
                            if(s[a] == '#'){
                                backCount += 2;
                            }
                        }
                    }

                    if(s[b] == '#'){
                        int backCount = 2;
                        while(backCount > 0 ){
                            b--;
                            backCount--;
                            if(s[b] == '#'){
                                backCount += 2;
                            }
                        }
                    }
                }
                else{
                    if(s[a] == t[b])
                        return false;
                    else{
                        a--;
                        b--;
                    }
                }

            }


            return true;
        }
    }
}