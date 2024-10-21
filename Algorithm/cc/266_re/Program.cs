using System;
using System.Linq;

public class Solution {
    public string solution(string X, string Y) {
        string answer = "";
        
        int x9 = X.Where(x => x == '9').Count();
        int x8 = X.Where(x => x == '8').Count();
        int x7 = X.Where(x => x == '7').Count();
        int x6 = X.Where(x => x == '6').Count();
        int x5 = X.Where(x => x == '5').Count();
        int x4 = X.Where(x => x == '4').Count();
        int x3 = X.Where(x => x == '3').Count();
        int x2 = X.Where(x => x == '2').Count();
        int x1 = X.Where(x => x == '1').Count();
        int x0 = X.Where(x => x == '0').Count();
        
        int y9 = Y.Where(x => x == '9').Count();
        int y8 = Y.Where(x => x == '8').Count();
        int y7 = Y.Where(x => x == '7').Count();
        int y6 = Y.Where(x => x == '6').Count();
        int y5 = Y.Where(x => x == '5').Count();
        int y4 = Y.Where(x => x == '4').Count();
        int y3 = Y.Where(x => x == '3').Count();
        int y2 = Y.Where(x => x == '2').Count();
        int y1 = Y.Where(x => x == '1').Count();
        int y0 = Y.Where(x => x == '0').Count();
        
        if (y9 >= x9) answer += new string('9',x9);
        else answer += new string('9',y9);
        
        if (y8 >= x8) answer += new string('8',x8);
        else answer += new string('8',y8);
        
        if (y7 >= x7) answer += new string('7',x7);
        else answer += new string('7',y7);
        
        if (y6 >= x6) answer += new string('6',x6);
        else answer += new string('6',y6);
        
        if (y5 >= x5) answer += new string('5',x5);
        else answer += new string('5',y5);
        
        if (y4 >= x4) answer += new string('4',x4);
        else answer += new string('4',y4);
        
        if (y3 >= x3) answer += new string('3',x3);
        else answer += new string('3',y3);
        
        if (y2 >= x2) answer += new string('2',x2);
        else answer += new string('2',y2);
        
        if (y1 >= x1) answer += new string('1',x1);
        else answer += new string('1',y1);
        
        if (y0 >= x0) answer += new string('0',x0);
        else answer += new string('0',y0);
        
        if (answer.Length == 0) answer = "-1";
        else if ((answer.Length == answer.Where(x => x=='0').Count()) && (answer.Length != 0)) answer = "0";
        
        return answer;
    }
}