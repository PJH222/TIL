using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string solution(string polynomial) {
        string answer = "";
        List<string> a = polynomial.Split(" ").ToList();
        
        int xx = 0; // x의 계수의 합
        int yy = 0; // 상수항의 합
        
        for(int i = 1 ;i<a.Count ; i++ ) {
            if (a[i] == "+") {
                if ((a[i - 1].IndexOf("x") == -1) && (a[i-1].Length > 1)) {
                    yy += int.Parse(a[i-1]);
                }
                else if ((a[i - 1].IndexOf("x") == -1) && (a[i-1].Length == 1)) {
                    yy += int.Parse((a[i-1]).ToString());
                }
                else if ((a[i - 1].IndexOf("x") != -1) && (a[i-1].Length == 1)) {
                    xx += 1;
                }
                else if ((a[i - 1].IndexOf("x") != -1) && (a[i-1].Length > 1)) {
                    string b = a[i-1].Substring(0,a[i-1].Length - 1);
                    xx += int.Parse(b.ToString());
                }
            }
            // Console.WriteLine("지나갑니다~~");
            if (i == a.Count - 1) {
                if ((a[i].IndexOf("x") == -1) && (a[i].Length > 1)) {
                    yy += int.Parse(a[i]);
                }
                else if ((a[i].IndexOf("x") == -1) && (a[i].Length == 1)) {
                    yy += int.Parse((a[i]).ToString());
                }
                else if ((a[i].IndexOf("x") != -1) && (a[i].Length == 1)) {
                    xx += 1;
                }
                else if ((a[i].IndexOf("x") != -1) && (a[i].Length > 1)) {
                    string b = a[i].Substring(0,a[i].Length - 1);
                    xx += int.Parse(b.ToString());
                }
                
            }
        }
        // Console.WriteLine("xx : {0} ,yy : {1}",xx,yy);
        
        if (a.Count == 1){
            if (a[0].IndexOf("x") == -1){
                yy = int.Parse(a[0].ToString());
            }
            else {
                if (a[0].Length != 1) {
                    string c = a[0].Substring(0,a[0].Length - 1);   
                    xx += int.Parse(c.ToString());
                }
                else if (a[0].Length == 1) xx += 1;
            }
        }
        
        if ((xx == 0) && (yy != 0)) {
            return yy.ToString();
        }
        else if ((yy == 0) && (xx != 0)){
            if (xx == 1) return "x";
            else return xx.ToString() + "x";
        }
        else if ((xx == 1) && (yy != 0)){
            return "x" + " " + "+" + " " + yy.ToString();
        }
        else if ((xx != 0) && (yy != 0)){
            return xx.ToString() + "x" + " " + "+" + " " + yy.ToString();
        }
        else if ((xx == 0 )&&(yy == 0)){
            return "";
        }
            
        
        return "xx.ToString() + " + " + yy.ToString()";
    }
}