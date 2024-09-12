using System;

public class Solution {
    public string solution(string myString) {
        string answer = "";
        string aa = "abcdefghijkl";
            
        for (int i = 0; i<myString.Length; i++){
            if (aa.IndexOf(myString[i]) != -1){
                answer += "l";
            }
            else {
                answer += myString[i];
            }
        }
            
        return answer;
    }
}