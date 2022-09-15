package SortAlgos; // put ot source
import java.util.Arrays;

public class SortAlgos {
    public static void main(String[] args){
        int[] arr = new int[]{2,1,4,7,22,-1,3,0};
        BubbleSort.sort(arr); // static methods do not need instantiation of the object, same as python @static decorator
        System.out.println("Bubble Sort:" + Arrays.toString(arr));

        int[] arr1 = new int[]{2,1,4,7,22,-1,3,0};
        SelectionSort.sort(arr1);
        System.out.println("Selection Sort:" + Arrays.toString(arr1));

        int[] arr2 = new int[]{2,1,4,7,22,-1,3,0};
        InsertionSort.sort(arr2);
        System.out.println("Insertion Sort:" + Arrays.toString(arr2));

        int[] arr22 = new int[]{2,1,4,7,22,-1,3,0};
        InsertionSort.recursiveSort(arr22,arr22.length);
        System.out.println("Recursive Insertion Sort:" + Arrays.toString(arr22));

        int[] arr3 = new int[]{2,1,4,7,22,-1,3,0};
        ShellSort.sort(arr3);
        System.out.println("Shell Sort:" + Arrays.toString(arr3));

        int[] arr4 = new int[]{2,1,4,7,22,-1,3,0};
        int[] merge_sort_arr4 = MergeSort.sort(arr4);
        System.out.println("Merge Sort:" + Arrays.toString(merge_sort_arr4));

        int[] arr5 = new int[]{2,1,4,7,22,-1,3,0};
        QuickSort.sort(arr5, 0, arr5.length-1);
        System.out.println("Quick Sort:" + Arrays.toString(arr5));

        int[] arr6 = new int[]{2,3,1,3,10,2,2,1,0,2,10,21,10};
        CountSort.sort(arr6); // assume ony positive integers
        System.out.println("Count Sort:" + Arrays.toString(arr6));

        int[] arr7 = new int[]{22,331,143,103,100,100,229,91,10,24,10,21,10};
        RadixSort radix = new RadixSort();
        int[] arr7_sorted = radix.sort(arr7);
        System.out.println("Radix Sort:" + Arrays.toString(arr7_sorted));


        int[] arr8 = new int[]{3,1,4,11,-10,3,2,111,23,3};
        Arrays.sort(arr8);
        System.out.println("Built-in Sort: "+ Arrays.toString(arr8));

    }

}
