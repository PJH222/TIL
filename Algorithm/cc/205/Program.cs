using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[,] dots) {
        int answer = 0;
        List<double> result = new List<double>();
        for (int i = 0 ; i<4 ; i++){
            int cnt = 0;
            List<double> tmp = new List<double>();
            // Console.WriteLine("다음 좌표 확인 작업 ㄱㄱ");
            
            for (int j = i + 1 ; j<4 ; j++){
                if (i == j){
                    continue;
                }
                double dx = dots[i,0] - dots[j,0];
                double dy = dots[i,1] - dots[j,1];
                double slope = dy/dx;
                Console.WriteLine("기울기 : {0}",slope);
                tmp.Add(slope);
                result.Add(slope);                
            }
        }
        
        foreach (double a in result){
            if (result.Where(x => x==a).Count() == 3){
                Console.WriteLine("점 3개가 한 직선위에 존재하는 경우");
                return 0;
            }
            else if (result.Where(x => x==a).Count() > 1){
                Console.WriteLine("평행하는 두 직선이 존재하는 경우");
                return 1;
            }
        }
        
        return answer;
    }
}