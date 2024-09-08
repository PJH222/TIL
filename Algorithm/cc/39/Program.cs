using System;

public class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        string a = "";
        string b = "";
        
        for (int i = 0 ; i < num_list.Length ; i++){
            if (num_list[i] % 2 == 1){
                a += num_list[i].ToString();
            }
            else{
                b += num_list[i].ToString();
            }
        }
        
        answer = int.Parse(a) + int.Parse(b);
        
        return answer;
    }
}