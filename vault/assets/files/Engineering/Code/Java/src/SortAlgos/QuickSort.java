package SortAlgos;

public class QuickSort {

    public static void sort(int arr[], int l, int r) {
        if (l >= r){
            return;
        }
        int index = pivot(arr,l,r);
        sort(arr, index ,r);
        sort(arr,l, index-1);

    }
    private static int pivot(int[] arr, int l, int r){
        int pivot = arr[r];
        int i = l-1;
        for (int j=l; j<r; j++){
            if (arr[j] < pivot){
                i ++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,r);
        return i+1;
    }

    private static void swap(int[] arr, int i, int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
