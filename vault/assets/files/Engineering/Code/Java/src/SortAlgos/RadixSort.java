package SortAlgos;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class RadixSort {
    public int[] sort(int[] arr){
        int[][] digits = new int[arr.length][];
        for (int i=0; i<digits.length; i++){
            digits[i] = getDigits(arr[i]);
        }
        Comparator cmp = new Comparator<int[]>() {

                @Override
                public int compare(int[] x, int[] y)
                {
                    if (x.length>y.length){
                        return 1;
                    }
                    else if (x.length<y.length){
                        return -1;
                    }
                    for (int i=0; i<x.length; i++){
                        if (x[i] > y[i]){
                            return 1;
                        }
                        else if (y[i] > x[i]){
                            return -1;
                        }
                    }
                    return 0;
                }
        };

        Arrays.sort(digits, cmp);

        int[] sorted_arr = new int[arr.length];

        for (int i = 0; i<digits.length; i++){
            sorted_arr[i] = toNumber(digits[i]);
        }

        return sorted_arr;
    }

    public int[] getDigits(int num){
        List<Integer> digits = new ArrayList<Integer>();
        while (num > 0){
            digits.add(num%10);
            num /= 10;
        }
        int i = 0;
        int j = digits.size()-1;

        while (i<j) {
            Integer swap = digits.get(i);
            digits.set(i,digits.get(j));
            digits.set(j,swap);
            i ++;
            j --;
        }

        int[] res = digits.stream().mapToInt(a -> a).toArray();
        return res;
    }

    public int[] fitness(int[] digits) {
        List<Integer> fit = new ArrayList<Integer>();
        fit.add(digits.length);
        for (Integer d:digits){
            fit.add(d);
        }
        int[] res = fit.stream().mapToInt(a -> a).toArray();
        return res;
    }

    public int toNumber(int[] digits){
        int number = 0;
        for (int i = 0; i<digits.length; i++) {
            number *= 10;
            number += digits[i];
        }
        return number;
    }

}
