package Udemy;
// Vector Class is synchronize that it is Thread safe ArrayList
// Vector came first
// Array class is not synchronized

import java.util.List;
import java.util.Vector;

// Synchronization has overhead
// If you want to run multiple threads use Vector (read and write is safe on different threads)

// If thread safety is not needed us ArrayList
public class VectorPlay {

    public static void playAround(){
        List<Employee> employeeVector = new Vector<>();
        employeeVector.add(new Employee("Ngo", "Cuong", 29));
        System.out.println("Vector: " + employeeVector);
    }  
}
