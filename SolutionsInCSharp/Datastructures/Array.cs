namespace SolutionsInCSharp
{
    public class Array
    {
        int[] arr;
        int length = 0;
        public Array(int n){
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
    }
}