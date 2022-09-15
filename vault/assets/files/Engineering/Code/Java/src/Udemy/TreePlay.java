package Udemy;

import java.util.TreeMap;

public class TreePlay {
    public static void playAround() {
        TreeMap<String,Integer> tree = new TreeMap<>();
        int val = 10;
        tree.put("key",val);
        System.out.println(tree);
//         TreeMap is an example of a SortedMap, which means that the order of the keys can be sorted, and when iterating over the keys, you can expect that they will be in order.

// HashMap on the other hand, makes no such guarantee. Therefore, when iterating over the keys of a HashMap, you can't be sure what order they will be in.
    }
}
