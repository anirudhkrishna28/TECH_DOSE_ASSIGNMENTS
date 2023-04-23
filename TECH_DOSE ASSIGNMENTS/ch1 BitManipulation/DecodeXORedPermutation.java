
class Solution {
    public int[] decode(int[] encoded) {
        int xorsum=0;
        for(int i=1;i<=encoded.length+1;i++)
        {
            xorsum^=i;
        }
        int sum1ton =0;
        for(int i=1;i<encoded.length;i+=2)
        {
          sum1ton^=encoded[i];
        } 
        int ans[] = new int[encoded.length+1];
        ans[0] = xorsum^sum1ton;
        for(int i=0;i<encoded.length;i++)
        {
          ans[i+1] = ans[i]^encoded[i];
        }
        return ans;
    }
}

public class DecodeXORedPermutation {
    
}
