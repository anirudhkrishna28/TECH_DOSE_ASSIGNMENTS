import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> h = new HashMap<>();
        int x = Integer.MIN_VALUE;
        int max = 0;
        for (Integer i : nums) {
            int val = h.getOrDefault(i, 0);
            h.put(i, val + 1);
            if (++val > x) {
                x = val;
                max = i;

            }
        }

        return max;
    }
}
