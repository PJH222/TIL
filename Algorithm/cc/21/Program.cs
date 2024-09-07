using System;

public class Solution {
    public string solution(string my_string) {
        string answer = "";
        char[] aa =  my_string.ToCharArray();
        
        for (int i = 0; i < aa.Length; i++){
            if (char.IsUpper(aa[i])){
                aa[i] = char.ToLower(aa[i]);
            }
            else{
                aa[i] = char.ToUpper(aa[i]);
            }
        }
        
    
        return String.Join("",aa);
        
        
        
    }
    
    
}