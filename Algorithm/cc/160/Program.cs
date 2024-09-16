using System;
using System.Linq;

public class Solution {
    public int[] solution(string my_string) {
        int[] answer = new int[52];
        string a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i<a.Length; i++){
            int b = my_string.Where(x => x==a[i]).Count();
            answer[i] = b;
        }
        
        return answer;
    }
}