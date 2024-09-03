using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string cipher, int code) {
        string answer = "";
        List<Char> aa = new List<Char>();
        
        for (int i = 1; i <= cipher.Length / code ; i++){
            // Console.WriteLine(i);
            // Console.WriteLine(cipher.Length);
            aa.Add(cipher[i * code - 1]);
            
        }
        
        return String.Join("",aa);
    }
}