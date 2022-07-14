import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println(sieve());
    }

    public static long sieve() {
        ArrayList<Boolean> arr = new ArrayList<>();
        arr.add(false);
        arr.add(false);
        for (int i = 2 ; i < 1000001 ; i++) {
            arr.add(true);
        }

        int sqrt = (int) Math.sqrt(1000000);

        for (int i = 2 ; i <=  sqrt; i++){
            if (arr.get(i)) {
                int temp = i+i;
                while (temp < 1000001) {
                    arr.set(temp , false);
                    temp += i;
                }
            }           
        }

        ArrayList<Integer> primes = new ArrayList<>();
        for (int i = 2 ; i <= 1000000 ; i++) {
            if (arr.get(i))     primes.add(i);
        }


        int maxNum = 0;
        long result = 0;
        for (int i = 0 ; i < primes.size() ; i++) {
            int sum = 0;
            for (int j = i ; j < primes.size();j++) {
                sum += primes.get(j);
                if (sum > 1000000)  break;
                if (!arr.get(sum))  continue; // O(1) constant time{    
                if(j-i+1 > maxNum ) {
                    maxNum = j-i+1;
                    result = sum;
                }
            }

        }
        return result;
    }
}
