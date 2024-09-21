using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        List<int> a = new List<int>();
        List<int> b = new List<int>();
        
        int maxx = 1;
        int minn = n * m;
        
        for (int i = 1 ; i<= (n >= m ? n : m) ; i++){
            if ((n % i == 0) && (m % i == 0) && (i >= maxx)){
                answer[0] = i;
            }
        }
        
        for (int i = (n >= m ? n : m) ; i<= n*m ; i++){
            if ((i % n == 0) && (i % m == 0) && (i <= minn)){
                answer[1] = i;
                break;
            }
            // Console.WriteLine(i);
        }
        
        
        
        
        return answer;
    }
}