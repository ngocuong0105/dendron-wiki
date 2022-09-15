package Udemy;

public class QueueArray {
    private int front = 0;
    private int back = 0;
    private Integer[] queue;

    public QueueArray(int capacity) {
        queue = new Integer[capacity];
    }

    public void add(int x){
        if (full()){
            Integer[] newQueue = new Integer[2*queue.length];
            System.arraycopy(queue, 0, newQueue, 0, queue.length);
            queue = newQueue;
        }
        queue[back] = x;
        back++;
    }

    public int remove(){
        int x = queue[front];
        queue[front] = null;
        front ++;
        if (empty()){
            back = 0;
            front = 0;
        }
        return x;
    }

    public boolean full(){
        return back == queue.length;
    }

    public int size() {
        return back - front;
    }

    public boolean empty() {
        return back == front;
    }

    public void printQueue() {
        for (int i=front; i<back; i++){
            System.out.println(queue[i]);
        }
    }
}
