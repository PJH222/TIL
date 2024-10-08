using System;
using System.Collections.Generic;
using System.Linq;
// 개오랜만에 공부하는 것 같다...
// 포기한 소수찾기는 다음에 기회되면 해보자...
public class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 1;
        int indict = 1; // while문 빠져나가는 기준
        List<int> aa = section.ToList();        
        int tmp = aa[0]; // 현재 위치 표시기
        while (aa.Count() > 0){
            if (tmp + m - 1 >= aa[0] ){
                aa.RemoveAt(0);
            }
            else {
                tmp = aa[0];
                answer ++;
                }
        }
        
        
        return answer;
    }
}