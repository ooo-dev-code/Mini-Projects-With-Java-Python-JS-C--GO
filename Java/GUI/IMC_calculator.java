import java.util.ArrayList;
import java.util.List;

import javax.swing.*;
import java.util.Random;
import java.time.LocalDateTime;
import java.util.Date;

public class main extends JFrame{

    public static void main(String[] args) {
        var choice = JOptionPane.showInputDialog("What do you want to do?    1. Calculate your IMC ");
        if ("1".equals(choice)){
            imc();
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
