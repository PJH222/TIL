using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int cnt = 0; // 현재 당첨번호와 일치하는 개수
        List<int> tmp1 = new List<int>{0,1,2,3,4,5,6};
        List<int> tmp2 = new List<int>{6,6,5,4,3,2,1};
        
        
        foreach (int i in win_nums){
            if (Array.IndexOf(lottos,i) != -1) cnt++;
        }
        int cnt_0 = lottos.Where(x=>x==0).Count();
        Console.WriteLine(cnt_0);
        
        answer[1] = tmp2[cnt];
        answer[0] = tmp2[cnt + cnt_0];
        return answer;
    }
}