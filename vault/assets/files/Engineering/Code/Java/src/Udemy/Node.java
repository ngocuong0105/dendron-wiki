package Udemy;

public class Node {

    private int val;
    private Node next;

    public Node(int val, Node next){
        this.val = val;
        this.next = next;
    }

    public int getVal(){
        return this.val;
    }

    public Node getNext(){
        return this.next;
    }

    public void setVal(int val){
        this.val = val;
    }


    public void setNext(Node next){
        this.next = next;
    }

    @Override
    public String toString() {
        return "Node [next=" + next + ", val=" + val + "]";
    }


}