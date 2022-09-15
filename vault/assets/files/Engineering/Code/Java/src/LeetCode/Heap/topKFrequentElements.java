package LeetCode.Heap;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

// Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/
// Customizable Priority Queue (min-max)
// Key Value pairs in the priority queue.

class topKFrequentElements {
    public static int[] solve(int[] nums, int k) {
        Map<Integer,Integer> counter = new HashMap<>();
        for (int num: nums){
            if (counter.containsKey(num)) {
                counter.replace(num,counter.get(num)+1);
            }
            else {
                counter.put(num,1);
            }
        }
        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap =
                 new PriorityQueue<>((a,b)->(a.getValue()-b.getValue()));
        
        for (Map.Entry<Integer,Integer> entry: counter.entrySet()) {
            maxHeap.add(entry);
            if (maxHeap.size() > k) {
                maxHeap.remove();
            }
        }
        
        int res[] = new int[k];
        int i = 0;
        for (Map.Entry<Integer,Integer> entry: maxHeap) {
            res[i] = entry.getKey();
            i++;
        }
        for (int num: res){
            System.out.println(num);
        }
        System.out.println(res.toString());
        return res;
    }
}