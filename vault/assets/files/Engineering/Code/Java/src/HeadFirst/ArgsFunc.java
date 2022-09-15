// file which gives example of how promitives and compound objects are passed as argument into functions
// everything is passed by value ()
package HeadFirst;
import java.util.Arrays;

public class ArgsFunc {
    public static void main(String[] args){
        int a = 5;
        int b = 6;
        modify(a,b); // primitives passed by value
        System.out.println(a);
        System.out.println(b);
        int[] intArray = new int[]{3,1,4,1,0};
        modifyArray(intArray); // also passed by reference BUT object's value is its reference
        System.out.println(Arrays.toString(intArray)); // 0th element is changed
        // thats to actually print the numbers you need toString method

        int[] intArrayB = new int[]{2};
        modifyArrayB(intArrayB); // also passed by reference
        System.out.println(Arrays.toString(intArrayB)); // intArrayB not changed as in the modifyArrayB function we assign new array

    }

    public static void modify(int a, int b) {
        a ++;
        b = 69;
    }

    public static void modifyArray(int[] array) {
        array[0] = 69;
    }

    public static void modifyArrayB(int[] arrayB) {
        arrayB = new int[]{2,3,9};
        System.out.println("kur:" + Arrays.toString(arrayB));
    }

}
