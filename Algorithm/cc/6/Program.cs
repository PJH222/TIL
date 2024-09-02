    using System;

    public class Solution {
        public int solution(int angle) {
            int answer = 0;

            if (angle == 180)
                answer = 4;
            else if (angle < 90)
                answer = 1;
            else if (angle == 90)
                answer = 2;
            else
                answer = 3;
            
            return answer;
        }
    }