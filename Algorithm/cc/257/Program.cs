using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int solution(int[] nums)
    {
        int answer = 0;
        List<int> result = new List<int>();
        int tmp = 0;
        for (int i=0; i<nums.Length ; i++){
            for (int j=i+1; j<nums.Length ; j++){
                for (int k=j+1; k<nums.Length ; k++){
                    tmp = nums[i] + nums[j] + nums[k];
                    
                    if (result.IndexOf(tmp) != -1) {
                        answer += 1;
                        continue;
                    }
                    
                    for (int x=2 ; x<(Math.Pow(tmp,0.5)) +1 ;x++){
                        if (tmp%x == 0) break;
                        if (x == (int)Math.Pow(tmp,0.5)) {
                            result.Add(tmp);
                            answer += 1;
                        }
                        
                    }
                }
            }
        }
        
        
        return answer;
    }
}