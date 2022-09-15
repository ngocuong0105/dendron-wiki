package SortAlgos;

public class SelectionSort {
    public static void sort(int[] arr){
        for (int i = arr.length-1; i>0; i--) {
            int largest = 0;
            for (int j = 0; j<=i ; j++) {
                if (arr[j] > arr[largest]) {
                    largest = j;
                }
            }
            swap(largest,i,arr);
        }

    }

    public static void swap(int i, int j, int[] arr) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

}
