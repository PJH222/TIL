using System;

public class Solution {
    public int solution(string number) {
        int answer = 0;
        int aa = 0;
        for (int i = 0 ; i<number.Length ; i ++){
            aa += int.Parse(number[i].ToString());
        }
        
        return aa%9;
    }
}