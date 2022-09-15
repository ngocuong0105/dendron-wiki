package Udemy;

import java.util.ArrayDeque;
import java.util.Deque;

public class IsPalindrome {

    public static boolean solve(String s){
        String text = s.replaceAll("[^A-Za-z]+", "");
        Deque<Character> original = new ArrayDeque<Character>();
        Deque<Character> reversed = new ArrayDeque<Character>();
        for (int i=0; i<text.length(); i++){
            original.push(text.charAt(i));
            reversed.add(text.charAt(i));
        }
        return original.toString().equals(reversed.toString());
    }
}
