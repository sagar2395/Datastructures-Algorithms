using System.Collections.Generic;

namespace SolutionsInCSharp{
    public class Solution24{
        public IList<string> LetterCombinations(string digits){
            
            
            foreach(char a in digits){

            }
            return new List<string>();
        }

        public Dictionary<int , List<char>> GetLettersDict(){
            Dictionary<int , List<char>> dict = new Dictionary<int, List<char>>();

            List<char> temp = new List<char>();
            dict[1] = temp;

            temp = new List<char>();
            temp.Add('a');
            temp.Add('b');
            temp.Add('c');

            dict[2] = temp;

            temp = new List<char>();
            temp.Add('d');
            temp.Add('e');
            temp.Add('f');

            dict[3] = temp;

            temp = new List<char>();
            temp.Add('g');
            temp.Add('h');
            temp.Add('i');

            dict[4] = temp;
            
            temp = new List<char>();
            temp.Add('j');
            temp.Add('k');
            temp.Add('l');

            dict[5] = temp;

            temp = new List<char>();
            temp.Add('m');
            temp.Add('n');
            temp.Add('o');

            dict[6] = temp;
            
            temp = new List<char>();
            temp.Add('p');
            temp.Add('q');
            temp.Add('r');
            temp.Add('s');

            dict[7] = temp;

            temp = new List<char>();
            temp.Add('t');
            temp.Add('u');
            temp.Add('v');
            
            dict[8] = temp;

            temp = new List<char>();
            temp.Add('w');
            temp.Add('x');
            temp.Add('y');
            temp.Add('z');

            dict[9] = temp;

            return dict;
        }
    }
}