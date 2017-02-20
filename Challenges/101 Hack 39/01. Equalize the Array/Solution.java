import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        int n=0;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        int[] array = new int[n];
        for(int i=0;i<n;i++)
        {
          array[i]=sc.nextInt();
        }
        // Create a hash map
        HashMap hm = new HashMap();
        for(int i=0;i<n;i++)
        {
          // Put elements to the map
          if(hm.get(new Integer(array[i]))!=null)
          {
            Integer currentValue = (Integer) hm.get(new Integer(array[i]));
            int currentIntValue = currentValue.intValue();
            hm.put(new Integer(array[i]), new Integer(currentIntValue +1));
          }
          else{
          hm.put(new Integer(array[i]), new Integer(1));
          }
        }
        // Get a set of the entries
      Set set = hm.entrySet();
      // Get an iterator
      Iterator i = set.iterator();
      //Define max
      int max = -9999;
      // Display elements
      while(i.hasNext()) {
         Map.Entry me = (Map.Entry)i.next();
         Integer gotValue = (Integer) me.getValue();
         int gotIntValue = gotValue.intValue();
         if(max<gotIntValue)
         {
           max=gotIntValue;
         }
      }
      int output=n-max;
      System.out.println(output);
    }
}
