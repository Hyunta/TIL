package section2;

import java.util.*;

public class q1 {

    public static int function(int number, int k) {

        for(int i = 1; i<= number; i++) {
            if (number % i == 0) {
                k--;
                if (k==0) return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int k = sc.nextInt();

        int k_div = function(number, k);
        System.out.println(k_div);
    }
}
