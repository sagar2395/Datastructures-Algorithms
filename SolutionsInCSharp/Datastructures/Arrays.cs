using System;

namespace SolutionsInCSharp
{
    public class Arrays
    {
        int[] arr;
        int length = 0;
        public Arrays(int n){
            arr = new int[n];
        }

        public int Get(int position){
            return arr[position];
        }

        public void Add(int value){
            arr[length] = value;
            length++;
        }

        public void Remove(){
            arr[length - 1] = 0;
            length--;
        }

        public void PrintArray(){

            Console.Write("[");
            foreach(var val in arr){
                Console.Write(val + " ");
            }
            Console.Write("]");
        }
    }
}