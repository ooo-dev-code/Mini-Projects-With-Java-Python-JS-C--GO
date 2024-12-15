import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        Scanner bank = new Scanner(System.in);
        Bank account = new Bank();

        System.out.print("Welcome to the bank ");
        System.out.println("1 - Enter Account");
        System.out.println("2 - Create Account");

        int user_response_0 = bank.nextInt();
        if (user_response_0 == 1) {
            enter_bank(user_response_0, bank, account);
        } else if (user_response_0 == 2) {
            
        }

    }

    static void enter_bank(int user_response_0, Scanner bank, Bank account) {
        System.out.print("Enter your code pin: ");
        int pin_response = bank.nextInt();

        if (account.pin == pin_response) {
            
            System.out.println("1 - Check Account");
            System.out.println("2 - Empty Account");
            System.out.println("Others - Exit");
            int user_response = bank.nextInt();

            switch (user_response) {
                case 1:
                    System.out.println("Account: " + account.savings);
                    System.out.println("1 - Add to Account");
                    System.out.println("2 - Take to Account");
                    System.out.println("Others - Exit");
                    int user_response_2 = bank.nextInt();
                    switch (user_response_2) {
                        case 1:
                            System.out.println("How much ?");
                            int value = bank.nextInt();
                            account.savings = account.savings + value;
                            System.out.println("Account: " + account.savings);
                            break;
                    
                        case 2:
                            System.out.println("How much ?");
                            int value = bank.nextInt();
                            account.savings = account.savings + value;
                            System.out.println("Account: " + account.savings);
                            break;
                    }
                
                case 2:
                    account.savings = 0;
                    System.out.println("Account: " + account.savings);
                    break;
            }

        } else {
            System.out.println("This is not the good pin");
        }

    }
        
}
