using System;
using System.Linq;

public class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = num_list.Sum() * num_list.Sum();
        int a = 1;
        for (int i = 0 ; i < num_list.Length; i++){
            a *= num_list[i];
        }
        
        if (a > sum){
            return 0;
        }
        
        return 1;
    }
}