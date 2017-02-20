import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] height = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = sc.nextInt();
        }
        // Create a hash map
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for (int i = 0; i < n; i++) {
            // Put elements to the map
            if (hm.get(Integer.valueOf(height[i])) != null) {
                Integer currentValue = (Integer) hm.get(Integer.valueOf(height[i]));
                int currentIntValue = currentValue.intValue();
                hm.put(Integer.valueOf(height[i]), Integer.valueOf(currentIntValue + 1));
            } else {
                hm.put(Integer.valueOf(height[i]), Integer.valueOf(1));
            }
        }
        // Get a set of the entries
        Set set = hm.entrySet();
        // Get an iterator
        Iterator i = set.iterator();
        //Define max
        int max = -9999;
        // Display elements
        while (i.hasNext()) {
            Map.Entry me = (Map.Entry) i.next();
            int gotIntValue = (Integer) me.getValue();
            if (max < gotIntValue) {
                max = gotIntValue;
            }
        }
        System.out.print(max);
    }
}
