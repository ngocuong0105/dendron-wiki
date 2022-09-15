package Udemy;

public class QueuePlay {
    public static void playAround(){
        QueueArray queueArray = new QueueArray(10);
        for (int i=2; i<20; i = i+2) {
            queueArray.add(i);
        }
        queueArray.remove();
        queueArray.printQueue();
    }
}
