import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;

public class Foo{

  public static void main(String[] args) {

    JFrame f = new JFrame("A JFrame");
    f.setSize(500, 500);
    f.setLocation(300,200);

    final JTextArea textArea = new JTextArea(1, 1);
    textArea.setLineWrap(true);
    textArea.setWrapStyleWord(true);
    f.getContentPane().add(BorderLayout.CENTER, textArea);
    JButton delete_b = new JButton("Delete");
    f.getContentPane().add(BorderLayout.NORTH, delete_b);

    JButton save_b = new JButton("Save");
    f.getContentPane().add(BorderLayout.WEST, save_b);

    save_b.addActionListener(new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        JFrame f = new JFrame("A JFrame");
        f.setSize(500, 100);
        f.setLocation(300,200);

        JLabel title = new JLabel("Name of your file in txt");
        f.getContentPane().add(BorderLayout.NORTH, title);
        final JTextArea saveArea = new JTextArea(1, 1);
        saveArea.setBackground(java.awt.Color.CYAN);
        f.getContentPane().add(BorderLayout.CENTER, saveArea);
        JButton save_b2 = new JButton("Save");
        f.getContentPane().add(BorderLayout.SOUTH, save_b2);

        save_b2.addActionListener(new ActionListener() {
          @Override
          public void actionPerformed(ActionEvent e) {

            String file_name = saveArea.getText();
            file_name = file_name.replace(" ", "_");
            try (java.io.FileWriter writer = new java.io.FileWriter(file_name + ".txt")) {
              System.out.println(file_name);
              writer.write(textArea.getText());
            } catch (java.io.IOException ex) {
              ex.printStackTrace();
            }
          }
        });

        f.setVisible(true);
      }
    });

    delete_b.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            textArea.setText("");
        }
    });

    f.setVisible(true);

  }

}
