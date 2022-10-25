/* Lea Lang
 * CS2011
 * Description: Write a program in which the "Nibble Monster"
 * keeps asking for nibbles until the user enters 'Q' or 'q'.
 */
import java.util.*;

public class NibbleMonsterWithSentinelControlledLoop{
  public static void main(String[] args){

    Scanner input = new Scanner(System.in);

    boolean keepRunning = true;

    do{

      System.out.println("Feed monster nibble :o ");

      //Will store the user's input
      char userEntry = input.next().charAt(0);

      //Checking if input is q or Q, and setting keepRunning to false
      if(userEntry == 'q' || userEntry == 'Q'){
        System.out.println("Bye Quitter.");
        keepRunning = false;
      
      //Checking if input is between A and F
      }else if(userEntry >= 'A' && userEntry <= 'F'){
        System.out.println("YUMM!");

      //Checking if input is between a and f
      }else if(userEntry >='a'  && userEntry <= 'f'){
        System.out.println("yum!");

      //Checking if input is between 0 and 9
      }else if(userEntry >= '0' && userEntry <= '9'){
        System.out.println("m04r f00d!");

      //print if its not a valid nibble
      }else{
        System.out.println("EWWW!");
      }

    }while (keepRunning);
    //after exiting the loop printing message to user
    System.out.print("You tried to poison me. ");
  }
}
