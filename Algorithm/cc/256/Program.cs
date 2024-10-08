using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] answers) {
        List<int> answer = new List<int>();
        List<int> tmp1 = new List<int>();
        List<int> tmp2 = new List<int>();
        List<int> tmp3 = new List<int>();
        
        for (int i=1; i<= 10000 ; i++){
            if (i%5 == 1){
                tmp1.Add(1);
            }
            else if (i%5 == 2){
                tmp1.Add(2);
            }
            else if (i%5 == 3){
                tmp1.Add(3);
            }
            else if (i%5 == 4){
                tmp1.Add(4);
            }
            else {
                tmp1.Add(5);
            }
        }
        for (int i=1;i<=10000;i++){
            if (i%2 == 1){
                tmp2.Add(2);
            }
            
            else if (i%8 == 0){
                tmp2.Add(5);
            }
            else if (i%8 == 6){
                tmp2.Add(4);
            }
            else if (i%8 == 4){
                tmp2.Add(3);
            }
            else if (i%2 == 0){
                tmp2.Add(1);
            }
        }
        // foreach (int i in tmp2) Console.Write(i);
        
        int cnt = 1;
        for (int i=1;i<=10000 ;i++){
            if (cnt <= 2) tmp3.Add(3);
            else if (cnt <= 4) tmp3.Add(1);
            else if (cnt <= 6) tmp3.Add(2);
            else if (cnt <= 8) tmp3.Add(4);
            else if (cnt <= 10) tmp3.Add(5);
            cnt += 1;
            
            if (cnt > 10) cnt = 1;
            
        }
        // foreach (int j in tmp3) {
        //         Console.Write(j);
        //         // Console.WriteLine();
        //     }
        
        int[] result = new int[3];
        
        for (int i=0 ;i<answers.Length; i++){
            if (answers[i] == tmp1[i]) result[0]++;
            if (answers[i] == tmp2[i]) result[1]++;
            if (answers[i] == tmp3[i]) result[2]++;
        }
        
        for (int i=0;i<3;i++){
            if ((result.Max() == result[i]) && (result.Where(x => x==result[i]).Count()==1)){
                answer.Add(i + 1);
                return answer.ToArray();
            }
            else if ((result.Max() == result[i]) && (result.Where(x => x==result[i]).Count()==2)){
                answer.Add(i+1);
            }
            else if ((result.Max() == result[i]) && (result.Where(x => x==result[i]).Count()==3)){
                answer.Add(1);
                answer.Add(2);
                answer.Add(3);
                return answer.ToArray();
            }
        }
            
            
            
        
        return answer.ToArray();
    }
}