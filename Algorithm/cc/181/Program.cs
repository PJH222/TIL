using System;

public class Solution {
    public int solution(int[,] dots) {
        int answer = 0;
        
        int maxx1 = -256;
        int min1 = 256;
        int maxx2 = -256;
        int min2 = 256;
        
        for (int i = 0 ; i < dots.GetLength(0) ; i ++)    {
            if (dots[i,0] > maxx1) maxx1 = dots[i,0];
            if (dots[i,0] < min1) min1 = dots[i,0];
        }
    
        for (int i = 0 ; i < dots.GetLength(0) ; i ++)    {
            if (dots[i,1] > maxx2) maxx2 = dots[i,1];
            if (dots[i,1] < min2) min2 = dots[i,1];
        }
        
        answer = (maxx2 - min2) * (maxx1 - min1);
        
        
        return answer;
    }
}