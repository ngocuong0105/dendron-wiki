package HeadFirst;

class Dog {
    private String dogName;
    private int dogSize;

    void bark(int numBarks){
        while (numBarks > 0) {
            System.out.println("Bau Bau");
            numBarks -= 1;
        }
    }

    public String getName(){
        return dogName;
    }

    public int getSize(){
        return dogSize;
    }

    public void setName(String name){
        dogName = name;
    }

    public void setSize(int size){
        if (size >=9 ){
            dogSize = size;
        }
        else {
            System.out.println("Invalid dog size");
        }
    }
}
