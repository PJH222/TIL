using System;

public class Solution {
    public int solution(int order) {
        int answer = 0;
        string aa = order.ToString();
        for (int i = 0 ; i < aa.Length ; i ++){
            if ((aa[i] % 3 == 0) && (aa[i] != '0')) {
                answer += 1;
                // 이해가 안가는데...? 어떨때는 48을 빼줘야하는거지?
                // 그리고 왜 != 0이 아닌 != '0' 으로 해줘야 하는거지...?
            }
            Console.WriteLine(aa[i]);
        }
        return answer;
    }
}