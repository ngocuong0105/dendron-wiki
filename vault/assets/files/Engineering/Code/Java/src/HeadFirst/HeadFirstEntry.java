package HeadFirst;

import java.util.Arrays;

class HeadFirstEntry {

    public static void main(String[] args) {
        // HEAD FIRST
        System.out.println("Factorial: " + Factorial.fact(5)); // static methods accessed from the Object class name
        System.out.println("Factorial recursive: " + Factorial.recursive_fact(5));
        System.out.println("Factorial tail recursive: " + Factorial.tail_recursive_fact(5,1));
        System.out.println("Cast byte to int: " + CastByteToInt.castByteToInt());

        BeerSong.playAround();

        // Working with a class
        Dog dog = new Dog();
        // dog.dogName = "Fido";  cannot access it as it is private
        dog.setName("Fido");
        dog.setSize(90);
        int numBarks = 3;
        dog.bark(numBarks); // not a static method hence accessed with the object reference
        System.out.println(numBarks); // numBarks passed in the bark method is a copy and is not changed.
        System.out.println("Dog Name: " + dog.getName());
        System.out.println("Dog Size: " + dog.getSize());
        String[] stringArray = {"Kur","Da"};
        int[] intArray = {1,2};
        System.out.println("Initialization of array: " + Arrays.toString(stringArray));
        System.out.println("Initialization of array: " + Arrays.toString(intArray));

    }
}
