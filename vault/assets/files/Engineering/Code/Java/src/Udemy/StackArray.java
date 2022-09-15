package Udemy;

import java.util.EmptyStackException;

// Stack Implementation is natural to be with a Linked List
// If you know maximum size of stack can use an array for implementing  a stack
public class StackArray {
    private Integer[] stack;
    private int top;

    public StackArray(int capacity) {
        stack = new Integer[capacity];
    }

    public void push(int x) {
        if (full()){
            // Resize stack
            Integer[] newStack = new Integer[2*stack.length];
            System.arraycopy(stack,0,newStack,0,stack.length);
            stack = newStack;
        }
        stack[top] = x;
        top += 1;
    }

    public Integer pop(){
        if (empty()) {
            throw new EmptyStackException();
        }
        Integer x = stack[--top];
        stack[top] = null;
        return x;
    }

    public boolean empty() {
        return top == 0;
    }

    public boolean full() {
        return top == stack.length;
    }

    public void printStack(){
        for (Integer x: stack) {
            if (x!=null){
                System.out.println(x);
            }
        }
    }

    public int size(){
        return top;
    }
}
