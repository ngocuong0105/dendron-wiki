package Udemy;



public class LinkedListPlay {

    public static void playAround(){
        Node node = new Node(0,null);
        System.out.println(node);

        LinkedListCustom linkedList = new LinkedListCustom(node);
        System.out.println("Linked List: "+ linkedList);

        Node newNode = new Node(69,null);
        linkedList.addToFront(newNode);
        System.out.println("Linked List Added node: "+ linkedList);

        System.out.println("Size of linked list: "+ linkedList.getSize());
        System.out.println("Is empty linked list: "+ linkedList.isEmpty());

        linkedList.deleteFront();
        System.out.println("Deleted fron node of a list: "+ linkedList);

    }

}
