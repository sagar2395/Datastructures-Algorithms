namespace SolutionsInCSharp{
    public class Solution18{
        public bool IsPalindrome(int x) {
        if(x < 0) return false;
        int reverse = 0;
        int temp = x;
        while(temp / 10 != 0){
            int remainder = temp % 10;
            reverse = reverse * 10 + remainder; 
            temp = temp / 10;
        };
        reverse = reverse * 10 + temp;
        return reverse == x;
    }
    }
}