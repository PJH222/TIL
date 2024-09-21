using System;
using System.Linq;

public class Solution {
    public string solution(string phone_number) {
        string answer = "";
        int a = phone_number.Length;
        for (int i = 0; i<a ;i++){
            if (i < a - 4){
                answer += "*";
            }
            else {
                answer += phone_number[i];
            }
        }
        
        return answer;
    }
}