using System;
using SolutionsInCSharp;
using System.Linq;

namespace SolutionsInCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Arrays arr = new Arrays(10);

            arr.Add(5);
            arr.Add(5);
            arr.Add(5);
            arr.Add(5);
            arr.Add(5);
            arr.Add(5);
            arr.Add(5);

            arr.PrintArray();
        

        }
    }
}
