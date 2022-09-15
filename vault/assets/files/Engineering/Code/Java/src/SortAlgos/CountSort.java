package SortAlgos;

import java.util.Arrays;

public class CountSort {
    public static void sort(int[] arr){
        int[] counts = getCounts(arr);
        // int[] output = new int[arr.length];
        int i = 0;
        int j = 0;
        while (j<counts.length) {
            while (counts[j] > 0) {
                arr[i] = j;
                counts[j] --;
                i++;
            }
            j++;
        }
        // return output;
    }

    private static int[] getCounts(int[] arr) {
        int[] counts = new int[Arrays.stream(arr).max().getAsInt()+1];
        for (int i = 0; i<counts.length; i++) {
            counts[i] = 0;
        }
        for (int i = 0; i<arr.length; i++){
            counts[arr[i]] ++;
        }
        System.out.println(Arrays.toString(counts));
        return counts;
    }

}
