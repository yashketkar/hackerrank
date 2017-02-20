import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc= new Scanner(System.in);
        int a[][];
        int n=sc.nextInt();
        a = new int[n][n];
        int main=0,sec=0;
        for(int i=0;i<n;i++)
            {
        for(int j=0;j<n;j++)
            {
            a[i][j]=sc.nextInt();
            if(i==j)
                main+=a[i][j];
            if(j==n-i-1)
                sec+=a[i][j];
        }
        }
        if(main<sec)
            System.out.println(sec-main);
        else
            System.out.println(main-sec);
    }
}
