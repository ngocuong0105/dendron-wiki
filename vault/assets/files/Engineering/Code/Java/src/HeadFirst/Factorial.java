package HeadFirst;

public class Factorial {

    public static int fact(int n) {
        int prod = 1;
        for (int i=1; i<=n; i++) {
            prod *= i;
        }
        return prod;
    }

    public static int recursive_fact(int n) {
        if (n == 1){
            return 1;
        }
        return n*recursive_fact(n-1);
    }

    public static int tail_recursive_fact(int n, int prod) {
        // Lisp has tail recursion optimization, recall you did not see any while/for loops there.
        // Java and Python does not have this optimization though
        if (n==1) {
            return prod;
        }
        return tail_recursive_fact(n-1, prod*n);
    }

}
