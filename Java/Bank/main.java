import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        Scanner bank = new Scanner(System.in);
        int pin = 1894;
        int savings = 1000;

        System.out.println("Welcome to the bank ");
        System.out.println("1 - Enter Account");
        System.out.println("2 - Create Account");

        int user_response_0 = bank.nextInt();
        if (user_response_0 == 1) {
            enter_bank(user_response_0, bank, pin, savings);
        } else if (user_response_0 == 2) {
            
        }

    }

    static void enter_bank(int user_response_0, Scanner bank, int pin, int savings) {
        System.out.print("Enter your code pin: ");
        int pin_response = bank.nextInt();

        if (pin == pin_response) {
            
            System.out.println("1 - Check Account");
            System.out.println("2 - Empty Account");
            System.out.println("Others - Exit");
            int user_response = bank.nextInt();

            if (user_response==1) {
                    System.out.println("Account: " + savings);
                    System.out.println("1 - Add to Account");
                    System.out.println("2 - Take to Account");
                    System.out.println("Others - Exit");
                    int user_response_2 = bank.nextInt();
                    if (user_response_2==1) {
                            System.out.println("How much ?");
                            int value = bank.nextInt();
                            savings = savings + value;
                            System.out.println("Account: " + savings);
                    }
                    
                    if (user_response_2==2) {
                        System.out.println("How much ?");
                        int values = bank.nextInt();
                        savings = savings - values;
                        System.out.println("Account: " + savings);
                    }
            }
            if (user_response==2) {
                savings = savings*0;
                System.out.println("Account: " + savings);
            }

        } else {
            System.out.println("This is not the good pin");
        }

    }
        
}
