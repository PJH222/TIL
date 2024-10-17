using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        Array.Sort(lost);
        Array.Sort(reserve);
        List<int> new_lost = lost.ToList();
        List<int> new_reserve = reserve.ToList();
        List<int> tmp = new List<int>();
        
        // 같은 학생이 있을 경우 제거.
        foreach (int i in new_reserve){
            if (new_lost.IndexOf(i) != -1){
                new_lost.RemoveAt(new_lost.IndexOf(i));
                tmp.Add(i);
            }
        }
        foreach (int i in tmp){
            new_reserve.Remove(i);
        }
        
        foreach (int i in new_reserve){
            if (new_lost.IndexOf(i-1) != -1){
                new_lost.Remove(i-1);
                tmp.Add(i);
            }
            else if (new_lost.IndexOf(i+1) != -1){
                new_lost.Remove(i+1);
                tmp.Add(i);
            }    
        }
        answer = n - new_lost.Count;
        
        return answer;
    }
}