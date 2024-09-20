using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] numlist, int n) {
        List<int> answer = new List<int>();
        List<int> diff = new List<int>();
        
        for (int i = 0 ; i < numlist.Length ; i++){
            diff.Add(Math.Abs(numlist[i] - n));
        }
        foreach (int i in diff) Console.WriteLine(i);
        
        for (int i = 0 ; i <= 10000 ; i++){
            if (diff.IndexOf(i) != -1){
                if ((diff.Where(x => (x == i)).Count() == 1) && (Array.IndexOf(numlist, i + n) != -1)) {
                    answer.Add(i + n);
                    Console.WriteLine("1번의 경우");
                    Console.WriteLine("diff[i] 값이 {0}일때 수행하며, {1}을 answer에 추가함",i,i+n);
                    Console.WriteLine();
                }
                else if ((diff.Where(x => (x == i)).Count() == 1) && (Array.IndexOf(numlist, i * -1 + n) != -1)) {
                    answer.Add(i * -1 + n);
                    Console.WriteLine("2번의 경우");
                    Console.WriteLine("diff[i] 값이 {0}일때 수행하며, {1}을 answer에 추가함",i,i * -1 + n);
                    Console.WriteLine();
                }
                else if ((diff.Where(x => (x == i)).Count() == 2) && (Array.IndexOf(numlist, i * -1 + n) != -1) && (answer.IndexOf(i * -1 + n) == -1)) {
                    answer.Add(i * 1 + n);
                    answer.Add(i * -1 + n);
                    Console.WriteLine("3번의 경우");
                    Console.WriteLine("diff[i] 값이 {0}일때 수행하며, {1}을 answer에 추가함",i,i * -1 + n);
                    Console.WriteLine();
                }
                
            }
        }
        
        return answer.ToArray();
    }
}