using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string solution(string letter) {
        string answer = "";
        Dictionary<string,string> morse = new Dictionary<string,string>{ {".-","a"},{"-...","b"},{"-.-.","c"},{"-..","d"},{".","e"},{"..-.","f"},
                {"--.","g"},{"....","h"},{"..","i"},{".---","j"},{"-.-","k"},{".-..","l"},
                {"--","m"},{"-.","n"},{"---","o"},{".--.","p"},{"--.-","q"},{".-.","r"},
                {"...","s"},{"-","t"},{"..-","u"},{"...-","v"},{".--","w"},{"-..-","x"},
                {"-.--","y"},{"--..","z"}
                };
        List<string> aa = letter.Split(" ").ToList();
        
        foreach (string str in aa){
            answer += morse[str];
        }
        return answer;
    }
}