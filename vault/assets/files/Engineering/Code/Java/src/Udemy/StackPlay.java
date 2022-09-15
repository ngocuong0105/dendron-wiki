package Udemy;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

// Stack Implementation is natural to be with a Linked List
// If you know maximum size of stack can use an array for implementing  a stack
public class StackPlay {

    public static void playAround(){

        StackArray myStack = new StackArray(10);
        myStack.push(30);
        myStack.push(31);
        myStack.pop();
        myStack.printStack();

        // using Java API to play around with a stack
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(69);
        stack.pop();
        for (int i = 0; i<10; i++){
            stack.push(i);
        }
        System.out.println(stack.toString());

        // Better implementation is using the deque
        Deque<Integer> stackq = new ArrayDeque<Integer>();
        stackq.push(999);
        System.out.println(stackq.toString());
    }

}
