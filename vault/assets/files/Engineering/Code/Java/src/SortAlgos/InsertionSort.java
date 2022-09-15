package SortAlgos;

public class InsertionSort {

    public static void sort(int[] arr) {
        for (int j = 0; j<arr.length; j++) {
            int newElement = arr[j];
            int i = j;
            while (i>0 && arr[i-1] > newElement) {
                arr[i] = arr[i-1];
                i--;
            }
            arr[i] = newElement;
        }

    }

    public static void recursiveSort(int[] arr, int numItems){
        if (numItems < 2) {
            return;
        }
        recursiveSort(arr, numItems-1);

        int newElement = arr[numItems-1];
        int i;
        for (i = numItems-1; i > 0 && arr[i-1] > newElement; i--){
            arr[i] = arr[i-1];
        }
        arr[i] = newElement;

    }
}
