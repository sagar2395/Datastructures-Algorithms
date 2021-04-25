using System;
using SolutionsInCSharp;

namespace SolutionsInCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Sagar chhabra");


            Solution rm = new Solution();
            int[] nums = new int[]{5,6,8,8,9,9,9,9,10};
            Console.WriteLine(rm.RemoveDuplicates(nums));


        }
    }
}
