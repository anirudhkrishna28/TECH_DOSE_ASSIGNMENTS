
class Solution {
    public int countPrimes(int n) {
        boolean []primes = new boolean[n];
        int cnt=0;
        for(int i=2;i<Math.sqrt(n);i++)
        {
            if(!primes[i])
            {
                for(int j=2;i*j<n;j++)
                {
                    primes[i*j]=true;
                }
            }
        }
        
        for(int i=2;i<n;i++)
        {
            if(!primes[i])
                cnt++;
        }
        return cnt;
    }
}
public class CountPrimes {
    
}
