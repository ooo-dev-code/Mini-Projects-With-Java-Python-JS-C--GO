import java.util.HashMap;
import java.util.Random;

public class dice {

    public static void main(String[] args) {

        HashMap<Integer, String> names = new HashMap<Integer, String>();
        names.put(1, "James");
        names.put(2, "John");
        names.put(3, "Jeremy");
        names.put(4, "Jeff");
        names.put(5, "Johnson");
        names.put(6, "Jenny");

        HashMap<Integer, String> cities = new HashMap<Integer, String>();
        cities.put(1, "Paris");
        cities.put(2, "NY");
        cities.put(3, "Washington");
        cities.put(4, "LA");
        cities.put(5, "OP");
        cities.put(6, "Carlos");

        Random random = new Random();

        int num = random.nextInt(6)+1;
        System.out.println("Name: " + names.get(num));

        int num2 = random.nextInt(99)+1;
        System.out.println("Age: " + num2);

        int num3 = random.nextInt(6)+1;
        System.out.println("City of birth: " + cities.get(num3));

    }
    
}
