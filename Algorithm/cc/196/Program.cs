using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr, int[] query) {
        // List로 변환
        List<int> answer = new List<int>();
        foreach (int i in arr) {
            answer.Add(i);
            // Console.WriteLine(i);
        }
        
        // Console.WriteLine();
        
        for (int i = 0 ; i < query.Length ; i++){
            if (i % 2 == 0){
                // 인덱스가 짝수 일 경우, answer[query값] 이후의 값 제거
                int xx = answer.Count;
                for (int j = 0 ; j < xx - query[i] - 1; j++){
                    // Console.WriteLine(answer.Count - query[i] - 1);
                    answer.RemoveAt(answer.Count - 1);
                    // Console.WriteLine(answer[answer.Count - 1]);
                    
                }
            }
            else {
                // 인덱스가 홀수 일 경우, answer[query값] 이전의 값 제거
                for (int j = 0 ; j < query[i]; j++){
                    answer.RemoveAt(0);    
                    // Console.WriteLine("공굴러가유~~");
                }
            }
            // 확인용
            // Console.WriteLine();
            // Console.WriteLine();
            // foreach (int z in answer) Console.WriteLine(z);
        }
        
        return answer.ToArray();
    }
}