package Udemy;
import java.util.Arrays;

public class ArrayPlay {
    public static void playAround()  {
        int[] intArray = new int[7]; // arrays are not dynamic data structure, cannot change size
        intArray[0] = 20;
        intArray[1] = 35;
        intArray[2] = -15;
        intArray[3] = 7;
        intArray[4] = 55;
        intArray[5] = 1;
        intArray[6] = -22;
        for (int i=0; i < intArray.length; i++) {
            System.out.println(intArray[i]);
        }
        // get me number 7 of the array
        for (int i=0; i< intArray.length; i++) {
            if (intArray[i] == 7) {
                System.out.println("7 found at index: " + i);
                break;
            }
        }
        String[] array = {"Kur","Pish"};
        System.out.println(Arrays.toString(array));
        String[] slicedArray = Arrays.copyOfRange(array, 0, array.length/2);
        System.out.println(Arrays.toString(slicedArray));
    }
}
