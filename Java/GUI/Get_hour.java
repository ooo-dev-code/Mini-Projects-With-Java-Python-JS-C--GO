import java.util.ArrayList;
import java.util.List;

import javax.swing.*;
import java.util.Random;
import java.time.LocalDateTime;
import java.util.Date;

public class Get_hour extends JFrame{

    public static void main(String[] args) {
        var choice = JOptionPane.showInputDialog("What do you want to do?    1. Calculate your IMC; 2. ROck Paper Scissors; 3. get the hour of the day. ");
        if ("1".equals(choice)){
            day();
        }
    }

    public static void day() {
        Date dt = new Date();
        int hours = dt.getHours();

        String hours_str = String.valueOf(hours);
        var output = hours_str + "h";

        JOptionPane.showMessageDialog(null, output);
    }
}
