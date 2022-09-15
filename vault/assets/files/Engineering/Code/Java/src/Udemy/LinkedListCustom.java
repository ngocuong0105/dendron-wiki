package Udemy;



public class LinkedListCustom {

    private Node head;
    private int size;

    public LinkedListCustom(Node head){
        this.head = head;
    }

    public void addToFront(Node node){
        node.setNext(this.head);
        this.head = node;
        size ++;
    }

    public void deleteFront(){
        if (isEmpty()){
            return;
        }
        this.head = this.head.getNext();
    }

    public int getSize(){
        return size;
    }


    public Boolean isEmpty(){
        return size == 0;
    }

    @Override
    public String toString() {
        return "LinkedList [head=" + head + "]";
    }


}
