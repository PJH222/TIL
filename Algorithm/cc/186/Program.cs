using System;

public class Example
{
    public static void Main()
    {
        String s;

        Console.Clear();
        s = Console.ReadLine();
        
        String a = "";
        foreach (char c in s){
            char x1 = (char.ToUpper(c) == c) ? char.ToLower(c) : char.ToUpper(c);
            a += x1.ToString();
        }
        
        Console.Write(a);
        
        
    }
}