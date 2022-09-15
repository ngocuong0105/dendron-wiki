package Udemy;

import java.util.LinkedList;

// Java have a built in Linked List data structure
public class LinkedListBuiltInPlay {

    public static void playAround(){
        LinkedList<Integer> listche = new LinkedList<Integer>();
        listche.addFirst(90);
        listche.addFirst(10);
        listche.addFirst(30);
        System.out.println(listche);

        listche.add(69); // add item at the end == listche.addLast(69)
        System.out.println(listche);

        listche.remove();// removes from the head == listche.removeFirst()
        System.out.println(listche);

        listche.removeLast();
        System.out.println(listche);

    }
}
