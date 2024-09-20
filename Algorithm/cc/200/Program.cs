using System;

public class Solution {
    public double solution(int[] common) {
        double answer = 0;
        if ((common.Length > 3) && (common[0] - common[1] == common[1] - common[2]) && (common[1] - common[2] == common[2] - common[3])) {
            answer = common[common.Length - 1] - common[1] + common[2];
            Console.WriteLine("경우 1");
        }
        
        else if (common[0] - common[1] == common[1] - common[2]) {
            answer = common[common.Length - 1] - common[0] + common[1];
            Console.WriteLine("경우 3");
        }
        
        else if ((common[1] / common[0] == common[2] / common[1])) {
            answer = common[common.Length - 1] * (common[1] / common[0]);
            Console.WriteLine("경우 2");
        }
        
        
        return answer;
    }
}
// 특이한건 else if 문 순서에 따라 답이 달라질 수 도 있다는 것...
// 아마도 조건문이 약간 허술하게 쓰여진 점과 int형에서 나눗셈에서 나오는 특이점 때문인 것 같다...