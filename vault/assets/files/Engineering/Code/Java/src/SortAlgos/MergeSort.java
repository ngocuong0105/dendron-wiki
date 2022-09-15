package SortAlgos;
import java.util.Arrays;

public class MergeSort {

    public static int[] sort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }

        int[] l = Arrays.copyOfRange(arr, 0, arr.length/2);
        int[] r = Arrays.copyOfRange(arr, arr.length/2, arr.length);

        l = MergeSort.sort(l);
        r = MergeSort.sort(r);
        return merge(l,r);
    }

    private static int[] merge(int[] left, int[] right) {
        int i = 0;
        int j = 0;
        int[] merged = new int[left.length+right.length];
        while (i<left.length || j<right.length) {
            int n1 = (i < left.length) ? left[i] : Integer.MAX_VALUE;
            int n2 = (j < right.length) ? right[j] : Integer.MAX_VALUE;
            if (n1 < n2) {
                merged[i+j] = n1;
                i ++;
            }
            else {
                merged[i+j] = n2;
                j++;
            }
        }
        return merged;
    }
}
