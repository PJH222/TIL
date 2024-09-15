using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1 ; i <= n ; i ++){
            if (n%i == 0){
                answer += 1;
                Console.WriteLine(i);
            }
        }
        return answer;
    }
}