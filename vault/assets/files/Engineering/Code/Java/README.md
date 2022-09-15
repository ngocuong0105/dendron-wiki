# Getting Started

Welcome to the VS Code Java world. Here is a guideline to help you get started to write Java code in Visual Studio Code.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

Meanwhile, the compiled output files will be generated in the `bin` folder by default.

> If you want to customize the folder structure, open `.vscode/settings.json` and update the related settings there.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).


## Arrays
```
int[] intArray = new int[7];
```
Arrays are stored in CONTIGUOUS block in memory - not scattered around randomly.
That is why you need to specify length when creating it - tells JVM how much memory to allocate.
Every element in the array takes similar memory (integers are 4 bytes = 2**32 bits).

Access indices is O(1). Say we a have array starting at address x. If each element of the array is
of length l, then the i-th element has address x+i*y.

Search value in array is O(n).
Add element to a full array O(n) - we need to create a new array. creating array is O(1) but we need
copy all elements in the new array.
Add element at specific index O(1).
Delete an element with known index by setting it to null O(1).
Delete element by shifting elements O(n).


## Arguments and Functions
In Java everything is strictly Pass-by-Value.

When argument is pass by value in function, the caller and callee act on two different objects.
Any changes to one variable don't modify the other.

When a parameter is pass-by-reference, the caller and the callee operate on the same object.
It means that when a variable is pass-by-reference, the unique identifier of the object is sent to the method.

Primitive variables store the actual values
Non-Primitives store the reference variables which point to the addresses of the objects.

Whenever an object is passed as an argument, an exact copy of the **reference variable** is created
which points to the same location of the object in heap memory as the original reference variable.
As a result of this, whenever we make any change in the same object in the method, that change is
reflected in the original object. **see ArgsFunc.java**

Tail recursion concept (available in Lisp not in Java and Python).

## General stuff

- creating objects process

The 3 steps of object declaration, creation and assignment
```
Dog myDog           =         new Dog();
(1. declare)    (3. assign)  (2. create an object)
```
1. Tells the JVM to allocate space for a reference variable, and  names that variable myDog.

2. Tells the JVM to allocate space for a new Dog object on the heap

3. Assigns the new Dog to the reference variable myDog.

## Useful code snippets

- primitives
```
<!-- Primitives:
integer: byte, short, int, ling (8,16,32,64 bits) all signed
floating point: float,double (32,64 bits) -->

float f =32.4f; // otherwise Java thinks it is a double

```
- initialize array
```
String[] stringArray = {"Kak","si"};
int[] intArray = {1,2};
String[][] arrays = new String[][] { array1, array2, array3, array4, array5 };
int[][] dirs = new int[][]{ {1,2}, {3,4} };
```
- copy array
```
String[] copyTo = new String[7];// need to create destination
System.arraycopy(copyFrom, 2, copyTo, 0, 7);

String[] copyTo = java.util.Arrays.copyOfRange(copyFrom, 2, 9);  
```
- arrays. You can't create arrays with a generic component type. Need to cast.
```
PCB[] res = (PCB[]) new Object[list.size()]; /* Not type-safe. */
```
- better use ArrayList
```
List<Set<Integer>> rows = new ArrayList<Set<Integer>>();
```

- convert array to string
```
System.out.println(java.util.Arrays.toString(copyTo));
```



- convert int[] to ArrayList<Integer>

```
int[] nums = int[]{2,1,3};
List<Integer> listNums = Arrays.stream(nums).boxed().toList();
```
- convert ArrayList<Integer> to int[]
```
list.stream().mapToInt(i -> i).toArray()
```

-initialize queue/deque
```
Queue<Integer> deque = new ArrayDeque<>();
```

- initialize declare hashmap = dictionary in python
```
Map<Character,Integer> mp = new HashMap<Character, Integer>;
```
- no need to declare type in the instantiation
```
 Map<Integer,HashSet<Integer>> map = new HashMap<>();
```

- map operations
```
mp.put(key, value);
mp.get(key);
mp.getOrDefault(key,defaultValue); // if key is not present returns defaultValue
mp.containsKey(id);
Object.hashCode(); // hash() function equivalent in Python
mp.putIfAbsent(key, value);
mp.forEach((k,v )- >System,out,print(k + v));
mp.remove(key);
```

```
LinkedHashMap<Integer,Integer>// another implementation of Map
.removeEldest() // extra method
```

- iterate a map
```
Map<String, Object> map = ...;

for (String key : map.keySet()) {
    // ...
}

for (Object value : map.values()) {
    // ...
}

for (Map.Entry<String, Object> entry : map.entrySet()) {
    String key = entry.getKey();
    Object value = entry.getValue();
    // ...
}
```
- cannot use arrays or primitives for keys in HashMaps

- no Python defaultdict in Java :(
```
// counter
String word = "keksneeseks"
Map<Character,Integer> counter = new HashMap<>();
for (Character ch: word.toCharArray()) {
    counter.put(counter.getOrDefault(ch,0)+1)
}s

// defaultdict(set)
Map<Character,HashSet<Integer>> map = new HashMap<>();
for (int[] log: logs){
    int id=log[0];
    int t=log[1];
    if(!map.containsKey(id)) map.put(id,new HashSet<>());
    map.get(id).add(t);
}
// logs is a list of lists [[id1,time1],[id2,time2]...]
// map records unique times for each id.
```

- count occupancies of a character in a string
```
int count = line.length() - line.replace("ch", "").length();
```


- initializing HashMap
```
import static java.util.Map.entry;
Map<String, String> test2 = Map.ofEntries(
    entry("a", "b"),
    entry("c", "d")
);

Map<Character,String> mp =  Map.of(
        '2', "abc", '3', "def", '4', "ghi", '5', "jkl",
        '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz");
```

- looping a HashMap keySet:
```
for (int i: mp.keySet()){
    System.out.println(mp.get(i));
}
```

- looping String
```
for(int i = 0, n = s.length() ; i < n ; i++) {
    char c = s.charAt(i);
}
```
```
for(char c : s.toCharArray()) {
    // process c
}
```

- printing Objects (Object is the mother class in Java, everything inherits from it)

```
System.out.println(object.toString());
```

- HOWEVER for arrays such as int[], String[], to print them you need:
```
System.out.println(Arrays.toString(array)); // just Java being inconsistent

```

-convert char to int
```
String element = "el5";
int x = element.charAt(-1)-'0'
```

- slice string

```
str.substring(1, 23)
```

- slice array
```
Arrays.copyOfRange(arr, 0, 2);
```

- concatenate two arrays
```
int[] first = Arrays.copyOfRange(nums,0,i);
int[] second = Arrays.copyOfRange(nums,i+1,nums.length);
int[] newnums = new int[first.length + second.length];
System.arraycopy(first, 0, newnums, 0, first.length);
System.arraycopy(second, 0, newnums, first.length, second.length);
```

- maximum of array
```
int max = Arrays.stream(array).max().getAsInt();
```

- sum of array
```
IntStream.of(a).sum();
```

- length, size of array, strings, ArrayLists:
```
array.length // not a method
arrayList.size() // method
string.length() // method
```

- slice ArrayList
```
new ArrayList(input.subList(0, input.size()/2))
```
- concatenate ArrayLists
```
Arraylist1.addAll(Arraylist2);
```

- StringBuilder, equivalent to ''.join() method in Python. avoid adding strings in a loop which is slow as it is creating new string objects in each iteration. Recall strings are immutable.

```
String[] words = new String[]{"Mama", "Ti", "E", "Gotinka"}
StringBuilder res = new StringBuilder();
for (String w: words) {
    res.append(w);
    res.append(" ");
}
System.out.println(res.toString().trim());
```
- reverse a string
```
String reversed = new StringBuilder(string).reverse().toString()
```

- compare strings
```
"apple".compareTo ("banana"). // returns less than 0 , 0, greater than 0
```


- one line if statement
```
if (boolean statement) doStuff ;
```

- sort array in-place
```
Arrays.sort(nums);
```

- sort array not in-place
```
int[] a2 = a.clone();
Arrays.sort(a2);
```

- compare values of an array
```
Arrays.equals(pattern,row) // unlike objects where you'd do obj1.equals(obj2)
```
- Arrays act on primitives only. They do not have any methods! Use Arrays library to do stuff with them.

- sort array with lambda function
```
Arrays.sort(months, (String a, String b) -> a.length() - b.length());
Arrays.sort(months, (a, b) -> a.length() - b.length());
```

- initialize ArrayList
```
ArrayList<String> places = new ArrayList<>(Arrays.asList("Buenos Aires", "Córdoba", "La Plata")); // FIXED LENGTH SAD
```

- Python initialization provides convenient syntax for creating lists:
```
lst = [ "a", "b", "c" ]
map = { "apple": 5, "banana": 7 }
```
- Java does not. It does provide a literal syntax for arrays:
```
String[] arr = { "a", "b", "c" };
```
- copy arrayList
```
List<Integer> newpath = new ArrayList<Integer>();
newpath.addAll(path);
```
- sort ArrayList
```
import java.utils.Collections;
Collections.sort(arrayList);

// alternatively
ArrayList.sort((Integer a, Integer b) -> b-a);
```
- wrap primitive to object
```
int i = 288;
Integer iWrap = new Integer(i);
```

- unwrap object to primitive
```
Integer i = new Integer(200);
int unWrapped = i.intValue();
```

- convert string to integer/ parsing using the Wrappers
```
String s = “2”;
int x = Integer.parseInt(s);
double d = Double.parseDouble(“420.24”);
boolean b = Boolean.parseBoolean(“True”);
```
- numbers to string
```
double d = 42.5;
String doubleString = "" + d;

double d = 42.5;
String doubleString = Double.toString(d);
```

- format numbers using the format method
```
String s = String.format("%, d", 1000000000); // will print 100,000,000
```
"%" says insert here, the "," says give me commas, d says decimal number.
"Take the second argument to this method, and format it as a decimal integer and insert commas ."

```
String s = String.format("I have %,.2f bugs to fix.", 476578.09876) // rounds and gives 476,578.10
```
"d" for decimal and "f" for floating point

Format specifier
%[argument number][flags][width][.precision]type

flags = comma
width = minimum number of characters that will be used
.precision = precision
type = double float

only type is REQUIRED (and % too)

- check if character is numeric:
```
Character.isDigit(str.charAt(i));
```

- keywords final - fixes the reference (arrow)
```
// Declaring a final array
final int arr1[] = { 1, 2, 3, 4, 5 };

// Declaring normal integer array
int arr2[] = { 10, 20, 30, 40, 50 };

// Assigning values to each other
arr2 = arr1; // allowed
arr1 = arr2; // not allowed
arr[1] = 69; //allowed
```


- assert statement message
```
assert (x >= 0) : "x is " + x; // prints x is -1
```
A Java assertion is turned off by default .
You have to enable assertions explicitly by passing -ea

- turn on assertions for Tests:
```
@Test(expected=AssertionError.class)
public void testAssertionsEnabled() {
    assert false;
}
```
- The assert statement should be used in implementation code, for defensive checks inside the implementation.
- JUnit assertTrue() methods should be used in JUnit tests, to check the result of a test.
- switch statement (with assert to make sure all cases are covered)
```
switch (vowel) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u': return "A";
    default: assert false;
}
```
Assertions test the internal state of your program to
ensure that it is within the bounds of its specification.
Assertion failures therefore indicate bugs.
External failures are not bugs, and there is no change you can make to your program in advance that will
prevent them from happening.
External failures should be handled using exceptions instead.

Many assertion mechanisms are designed so that assertions aue executed only during testing and debugging, and
turned off when the program is released to users. Java’s assert statement behaves this way. The advantage of this
approach is that you can write very expensive assertions that would otherwise seriously degrade the performance of
your program

- ternary operator
```
(boolean expression) ? valueIfTrue : valueIfFalse
```

TreeMap is an example of a SortedMap, which means that the order of the keys can be sorted, and when iterating over the keys, you can expect that they will be in order.
```
TreeMap<String,Integer> tree = new TreeMap<>();
```
HashMap on the other hand, makes no such guarantee. Therefore, when iterating over the keys of a HashMap, you can't be sure what order they will be in.

- HashMap: Lookup-array structure, based on hashCode(), equals() implementations, O(1) runtime complexity for inserting and searching, unsorted
- TreeMap: Tree structure, based on compareTo() implementation, O(log(N)) runtime complexity for inserting and searching, sorted


- initialize Heap, PriorityQueue = min Heap!
```
PriorityQueue<Integer> pq = new PriorityQueue<>();
```

- add elements in PriorityQueue
```
pq.add(25);
pq.add(2)
```
- see first element
```
pq.peek(); // return 2
```
- remove root from priority queue
```
pq.remove(); // removes and returns min element
```
- poll root
```
pq.poll(); // the same as remove();
```
- with remove we can specify which element to remove if it exists:
```
pq.add(69);
pq.remove(69);
```
- pass comparator in the priority queue
```
// Java program to demonstrate working of
// comparator based priority queue constructor
import java.util.*;
  
public class Example {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        // Creating Priority queue constructor having
        // initial capacity=5 and a ListComparator instance
        PriorityQueue<Student> pq = new
             PriorityQueue<Student>(5, new ListComparator());
                  
             
        }
    }
}

class ListComparator implements Comparator<List<Integer>>{
            public int compare(List<Integer> s1, List<Integer> s2) {
                if (s1.get(0) > s2.get(0))
                    return 1;
                else if (s1.get(0) < s2.get(0))
                    return -1;
                return 0;
                }
        }
```
- convert priority queue to array
```
Object[] integers = pq.toArray();
```


