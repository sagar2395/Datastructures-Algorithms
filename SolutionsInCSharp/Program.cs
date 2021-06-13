using System;
using SolutionsInCSharp;
using System.Linq;

namespace SolutionsInCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a = new int[]{5,10,12,2,6,45,78,85,1,0,5,52,78};

            double b = a.Where(x => x % 2 == 0).Select(x => x * 100).OrderBy(x => x).Skip(2).Take(3).Min();

            //foreach(var i in b){
                Console.WriteLine(b);
            //}

            Console.WriteLine("End of Program");
        

        }
    }
}
