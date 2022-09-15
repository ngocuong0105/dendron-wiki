package Udemy;

import java.util.Arrays;

public class SearchAlgoPlay {

    public void playAround() {
        int[] array = new int[]{2,3,1,0,-10};
        Arrays.sort(array);
        int target = 0;
        System.out.println("Linear search index: " + LinearSearch(array, target));
        System.out.println("Binary search index: " + BinarySearch(array, target));
    }

    public int LinearSearch(int[] array, int target) {
        for (int i=0; i< array.length; i++) {
            if (array[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public int BinarySearch(int[] array, int target) {
        int l = 0, r = array.length-1;
        while (l < r) {
            int m = (l + r) / 2;
            if (array[m] >= target) r = m;
            else l = m+1;
        }
        if (array[l] == target) return l;
        else return -1;
    }

}
