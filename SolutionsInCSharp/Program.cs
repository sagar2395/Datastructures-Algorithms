using System;
using SolutionsInCSharp;
using System.Linq;

namespace SolutionsInCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution25 rs = new Solution25();

            int[] a = new int[]{5 , 13, 18, 24, 36};
            int[] b = new int[]{8 , 12, 14, 28, 39, 53};
        
            int[] c = rs.MergeSortedArrays(a , b);
            
            foreach(var val in c){
                Console.Write(val + " ");
            }
        }
    }
}
