package Udemy;

public class DoubleNode {

    private int val;
    private DoubleNode prev;
    private DoubleNode next;

    public DoubleNode(int val, DoubleNode prev, DoubleNode next) {
        this.val = val;
        this.prev = prev;
        this.next = next;
    }

    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }

    public DoubleNode getPrev() {
        return prev;
    }

    public void setPrev(DoubleNode prev) {
        this.prev = prev;
    }

    public DoubleNode getNext() {
        return next;
    }

    public void setNext(DoubleNode next) {
        this.next = next;
    }

    @Override
    public String toString() {
        return "DoubleNode [next=" + next + ", prev=" + prev + ", val=" + val + "]";
    }



}
