
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

        Random random = new Random();

        int num = random.nextInt(6)+1;
        System.out.println("Name: " + names.get(num));

        int num2 = random.nextInt(99)+1;
        System.out.println("Age: " + num2);

    }
    
}
