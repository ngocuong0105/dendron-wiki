package Udemy;

public class DoubleLinkedListPlay {

    public static void playAround(){
        DoubleNode node = new DoubleNode(69,null,null);
        DoubleNode nxt = new DoubleNode(9,null,null);
        DoubleNode prev = new DoubleNode(10,null,null);
        node.setVal(69);
        node.setNext(nxt);
        node.setPrev(prev);

        System.out.println(node);
    }
}
