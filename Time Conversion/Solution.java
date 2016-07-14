import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        /* StringBuilder sb = new StringBuilder(time);
        String hh = sb.substring(0,2);
        int h = Integer.parseInt(hh);
        String ap = sb.substring(8);
        if(ap=="PM")
            h+=12;
        if (h<10)
            sb.setCharAt(0,'0');
            sb.setCharAt(1,h);
        else
            {

            String nu = Integer.toString(h);
        }System.out.println(sb);   */
        try{
            Scanner sc= new Scanner(System.in);
        String time = sc.next();
         SimpleDateFormat displayFormat = new SimpleDateFormat("HH:mm:ss");
       SimpleDateFormat parseFormat = new SimpleDateFormat("hh:mm:ssa");

            Date date = parseFormat.parse(time);
            System.out.println(displayFormat.format(date));}
        catch(Exception e){}
    }
}
