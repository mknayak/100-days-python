using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'getRemovableIndices' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. STRING str1
     *  2. STRING str2
     */

    public static List<int> getRemovableIndices(string str1, string str2)
    {
        Regex pattern= new Regex("[a-z]+");
        List<int> result=new List<int>();
        if ( str1.Length>=2 && str1.Length <= (2*100000) && pattern.IsMatch(str1))
        {
            if (str2.Length>=1 && str2.Length <= (2*100000) && pattern.IsMatch(str2) && str1.Length == 1+ str2.Length)
            {           
              for(int i=0;i<str1.Length;i++){
                string str1_new= str1.Substring(0,i);
                if(i< str1.Length-1)
                {
                    str1_new = str1_new + str1.Substring(i+1);
                }
                if(str2.Equals(str1_new)){
                    result.Add(i);
                }
              }
               
            }
        }
        
        if (result.Count==0)
            result.Add(-1);        
        return result;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        while (true)
        {
            try
            {
                string str1 = Console.ReadLine();
                string str2 = Console.ReadLine();

                List<int> result = Result.getRemovableIndices(str1, str2);

                Console.WriteLine(String.Join("\n", result));
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        } 
    }
}
