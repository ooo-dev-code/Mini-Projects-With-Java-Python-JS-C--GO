import java.util.ArrayList;
import java.util.List;

import javax.swing.*;
import java.util.Random;
import java.time.LocalDateTime;
import java.util.Date;

public class All extends JFrame{

    public static void main(String[] args) {
        var choice = JOptionPane.showInputDialog("What do you want to do?    1. Calculate your IMC; 2. ROck Paper Scissors; 3. get the hour of the day. ");
        if ("1".equals(choice)){
            imc();
        }
        if ("2".equals(choice)){
            rps();
        }
        if ("3".equals(choice)){
            day();
        }
    }

    public static void imc() {

        var height = JOptionPane.showInputDialog("What is your height (in centimeters)?");
        var weight = JOptionPane.showInputDialog("What is your weight (in kg)?");

        double heightInMeters = Double.parseDouble(height) / 100;
        double weightInKg = Double.parseDouble(weight);

        double IMC = (weightInKg / Math.pow(heightInMeters, 2));

        String result;
        if (IMC > 18 && IMC < 25) {
            result = "This is a normal IMC";
        } 
        if (IMC < 18) {
            result = "You're Anorexic";   
        } else {
            result = "You're Obese";
        }

        var output = "Your IMC is " + IMC + ". " + result;


        JOptionPane.showMessageDialog(null, output);
    
    }
    public static void rps() {

        Random rand = new Random();
        int computer_choice_int = rand.nextInt(3)+1;
        String computer_choice = String.valueOf(computer_choice_int);

        String computer_response = "";
        if ("1".equals(computer_choice)) {
            computer_response = "Rock";
        }
        if ("2".equals(computer_choice)) {
            computer_response = "Paper";
        }
        if ("3".equals(computer_choice)) {
            computer_response = "Scissors";
        }

        var human_choices = JOptionPane.showInputDialog("Rock (type 1);      Paper(type 2);     Scissors(type 3)");
        String human_choice = "";
        if ("1".equals(human_choices)) {
            human_choice = "Rock";
        }
        if ("2".equals(human_choices)) {
            human_choice = "Paper";
        }
        if ("3".equals(human_choices)) {
            human_choice = "Scissors";
        }

        String result = "";
        if (computer_response.equals(human_choice)) {
            result = "Draw";
        }


        if ("Rock".equals(human_choice) && "Scissors".equals(computer_response)) {
            result = " YOU WON !!!!!!!";
        }
        if ("Paper".equals(human_choice) && "Rock".equals(computer_response)) {
            result = " YOU WON !!!!!!!";
        }
        if ("Scissors".equals(human_choice) && "Paper".equals(computer_response)) {
            result = " YOU WON !!!!!!!";
        }

        
        if ("Scissors".equals(human_choice) && "Rock".equals(computer_response)) {
            result = " You lost...";
        }
        if ("Rock".equals(human_choice) && "Paper".equals(computer_response)) {
            result = " You lost...";
        }
        if ("Paper".equals(human_choice) && "Scissors".equals(computer_response)) {
            result = " You lost...";
        }

        var output = "The computer chose " + computer_response + ".    You chose " + human_choice + ".            " + result; 

        JOptionPane.showMessageDialog(null, output);

    }


    public static void day() {
        Date dt = new Date();
        int hours = dt.getHours();

        String hours_str = String.valueOf(hours);
        var output = hours_str + "h";

        JOptionPane.showMessageDialog(null, output);
    }
}
