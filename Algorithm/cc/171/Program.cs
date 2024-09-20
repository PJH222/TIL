using System;
using System.Linq;
using System.Text;

public class Solution {
    public string solution(string my_string, int[,] queries) {
        string answer = "";
        // StringBuilder str = new StringBuilder();
        
        for (int i = 0 ; i < queries.GetLength(0) ; i++){
            StringBuilder str = new StringBuilder();

            int start = queries[i,0];
            int end = queries[i,1];
            
            string a = my_string.Substring(0,start);
            
            string b = my_string.Substring(start,end - start + 1);
            
            b = new string(b.Reverse().ToArray());
            
            string c = my_string.Substring(end + 1,my_string.Length - end - 1);
            
            // my_string = a+b+c;
            str.Append(a);
            str.Append(b);
            str.Append(c);
            my_string = str.ToString();

        }
        
        return my_string;
    }
}   