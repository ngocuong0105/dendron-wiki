package SortAlgos;

public class ShellSort {
    public static void sort(int[] arr){
        int gap = arr.length/2;
        while(gap > 0){
            int i = gap;
            while (i < arr.length) {
                int newElement = arr[i];
                int j = i;
                while( j >= gap && arr[j-gap]>newElement){
                    arr[j] = arr[j-gap];
                    j -= gap;
                }
                i ++;
                arr[j] = newElement;
            }
            gap /= 2;
        }
    }
}
