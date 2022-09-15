package Udemy;
// Lists are Abstract Data Type - when there is ADT there is INTERFACE
// ADT is the mathematical Idea , Abstract Data Structure is the actual data object (class).
// stack in Python is a ADT, the actual data structure is a dynamic python arrays
// ADT are often implemented using an INTERFACE in Java
// List interface is a Java thing
// Few classes using the List Interface: LinkedList, ArrayList

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
// Array list is a RESIZABLE array.
// Array lists have SIZE and CAPACITY
// Size = actual number of objects in the ArrayList
// Capacity = initial size of the backing array behind the ArrayList
// Capacity = maximum size before it needs to be resized if its full
public class ArrayListPlay {

    public static void playAround() {
        List<Integer> integerList = new ArrayList<Integer>();
        integerList.add(69);
        integerList.add(22);
        Collections.sort(integerList);
        // integerList.sort((Integer a, Integer b) -> b-a);
        System.out.println("Integer list:" + integerList); // prints a string rather than the reference (differs from printing array int[])

        List<Employee> employeeList = new ArrayList<Employee>();
        // add elements in the end of the ArrayList
        employeeList.add(new Employee("Kur", "VO", 999));
        employeeList.add(new Employee("Da","Ti",222));
        employeeList.add(new Employee("Mamma", "RA", 9));
        System.out.println("List of employees:" + employeeList);

        // lambda expression for printing
        employeeList.forEach(employee -> System.out.println("Employee:" + employee));

        // get and set elements in a list -> O(1)
        System.out.println("Get element of a list using list.get(i): " + employeeList.get(2));

        employeeList.set(0, new Employee("NNN", "LastName", 21));

        System.out.println("Size of List list.size():" + employeeList.size());

        // convert ArrayList to an array
        // Object[] empArray = employeeList.toArray(); // do this if you dont specify the type of the array
        Employee[] empArray = employeeList.toArray(new Employee[3]);
        System.out.println("Employee List converted to an Array:" + Arrays.toString(empArray));

        for (Employee emp: empArray) {
            System.out.println(emp);
        }

        // contains method for the ArrayList - O(n)
        System.out.println("Check is in element with .contains(): " + employeeList.contains(new Employee("Da", "Ti", 222))); // gives false as it is searching for the reference (bits)
        // need to write your own equals method (see override of hashcode and equals methods in the Employee Class - generated boilerplate code)

        //indexOf - O(n)
        System.out.println("Find index of an element with .indexOf: " + employeeList.indexOf(new Employee("Da", "Ti", 222)));

        // remove element
        employeeList.remove(1);


        // automatic wrap unwrap from object to primitives
        ArrayList<Integer> kur = new ArrayList<Integer>();
        int x = 0;
        kur.add(x);
        System.out.println(kur.get(0).getClass()); // still wrapped Integer type
        int y = kur.get(0); // unwraps
    }
}
