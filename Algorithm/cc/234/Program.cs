using System;

class Solution
{
    public long solution(int price, long money, int count)
    {
        int cnt = 0;
        long result = 0;
        int aa = price;
        while (cnt != count){
            result += price;
            price += aa;
            cnt += 1;
            
        }
        if (result - money < 0){
            return 0;
        }
        
        return result - money;
    }
}