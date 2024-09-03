using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int money) {
        int[] answer = new int[] {};
        List<int> bb = new List<int>();
        
        int aa = 0;
        for (int i=0; i <= 1000; i++){
            if (money >= 5500){
                aa += 1;
                money -= 5500;
            }
            else if (money < 5500){
                break;
            }
        }
        
        Console.WriteLine(money);
        Console.WriteLine(aa);
        
        bb.Add(aa);
        bb.Add(money);
        
        return bb.ToArray();
    }
}

// 비효율의 끝판왕 아니냐;; 파이썬 갓갓