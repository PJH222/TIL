using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[] {};
        List<List<int>> tmp1 = new List<List<int>>();
        int a = arr.Where(x => x == 2).Count();
        for (int i = 0; i<arr.Length ; i++){
            if (arr[i] != 2) continue;
            int cnt = 0;
            List<int> tmp2 = new List<int>();
            for (int j = i; j<arr.Length ;j++){
                tmp2.Add(arr[j]);
                cnt += 1;
                // Console.WriteLine(arr[j]);
                if ((tmp2[0] == 2)&&(tmp2[cnt - 1] == 2)){
                    tmp1.Add(tmp2);
                    // Console.WriteLine("asdsd");
                }
                if (tmp2.Where(x => (x == 2)).Count() == a) break;
            }
        }
        foreach (List<int> c in tmp1){
            if ((c[0] == 2)&&(c[c.Count - 1] == 2)) {
                if (answer.Length < c.Count) answer = c.ToArray();
            }
        }
        if (answer.Length == 0) return new int[]{-1};
        return answer;
    }
}

// 최적화 실패로 다시 풀어야함...
