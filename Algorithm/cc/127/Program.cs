using System;

public class Solution {
    public string solution(string myString, string pat) {
        string answer = "";
        string a = myString.Substring(0,myString.LastIndexOf(pat) + pat.Length);
        // string b = myString.Substring(myString.IndexOf(pat),myString.Length - myString.IndexOf(pat));
        Console.WriteLine(a);
        // Console.WriteLine(b);
        
        // if (a.Length>b.Length) return a;
        // else return b;
        
        return a;
    }
}

// 문제를 잘못이해하고 풀었다...