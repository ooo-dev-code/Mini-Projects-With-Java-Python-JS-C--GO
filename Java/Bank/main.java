import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        int account = 1000;
        Scanner bank = new Scanner(System.in);
        System.out.print("Enter your code pin: ");
        int pin = 1894;
        int pin_response = bank.nextInt();

        if (pin == pin_response) {
            System.out.println("1 - Check Account");
            System.out.println("Others - Exit");
            int user_response = bank.nextInt();
            switch (user_response) {
            case 1:
                System.out.println("Account: " + account);

                System.out.println("1 - Add to Account");
                System.out.println("Others - Exit");
                int user_response2 = bank.nextInt();
                switch (user_response2) {
                    case 1:
                        System.out.println("How much");
                        int value = bank.nextInt();
                        account = account + value;
                        System.out.println("Account: " + account);
                        break;
                    default:
                        break;
                }
            }
        } else {
            System.out.println("This is not the good pin");
        }
    }
}
