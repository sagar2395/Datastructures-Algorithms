using System;

namespace SolutionsInCSharp{
    public class Solution22{
        public string Convert(string s, int numRows){
            if(numRows == 0) return s;

            int offset = numRows * 2 - 2;
            string result = "";
            int index = 0;
            int row = 1;
            int first = 0;
            int second = 0;

            while(row <= numRows){
                Console.WriteLine($"Row: {row}");
                first = offset - (row - 1) * 2;
                Console.WriteLine($"First : {first}");

                second = offset - first;
                Console.WriteLine($"Second : {second}");

                Console.WriteLine($"index : {index}");
                while(index < s.Length){
                    result += s[index];
                    if(row == 1 || row == numRows){
                        index += offset;
                    }
                    else{
                        index = index + first;
                        if(index < s.Length){
                            result += s[index];
                            index += second;
                        }
                    }
                    Console.WriteLine($"Result: {result}");
                }
                row++;
                index = row - 1;
            }

            return result;
        }
    }
}