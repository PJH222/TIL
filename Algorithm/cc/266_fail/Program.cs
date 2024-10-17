using System;
using System.Linq;

public class Solution {
    public string solution(string X, string Y) {
        string answer = "";
        string xx = new String(X.ToCharArray().OrderByDescending(x=>x).ToArray());
        string yy = new String(Y.ToCharArray().OrderByDescending(x=>x).ToArray());
        
        
        foreach (char c in xx){
            if ((yy.IndexOf(c) != -1)&&(yy.Where(x=> x==c).Count()>answer.Where(x=> x==c).Count())) {
                answer += c;
        }
                }
        if ((answer.Where(x => x=='0').Count() == answer.Length) && (answer.Length != 0)){
            answer = "0";
        }
        else if (answer.Length == 0) {
            answer = "-1";
            return answer;
        }
        
        // string b = new String(answer.ToCharArray().OrderByDescending(x=>x).ToArray());
        
        
        
        return answer;
    }
}