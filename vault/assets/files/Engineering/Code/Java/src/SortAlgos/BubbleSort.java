package SortAlgos;
public class BubbleSort {
    // Stable sorting algo, if you change line 9  to >= wont be stable
    public static void sort(int[] intArray)  {
        for (int j=intArray.length-1; j>=0; j--) {
            for (int i=0; i<j; i++) {
                if (intArray[i] > intArray[i+1]) {
                    swap(intArray,i,j); // intArray address is passed in the function hence changed
                }
            }
        }
    }

    public static void swap(int[] array, int i, int j) {
        if (i == j) {
            return;
        }
        int tmp = array[i];
        array[i] = array[i+1];
        array[i+1] = tmp;
    }

}
