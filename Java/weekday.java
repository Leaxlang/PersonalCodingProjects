/*
 * author: Lea
 * class: 2011
 * date: 9/14/2022
 * description: Asking the user for the current day of the week, and another day in the future. 
 * Then calculating what weekday the future day will be.
 */

import java.util.*;

public class weekday{
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);    

    System.out.println("What day of the week is today?");
    String startDay = input.next();
    int dayNumber = 0;

    switch(startDay){
      case "Monday":
        dayNumber = 0;
        break;
      case "Tuesday":
        dayNumber = 1;
        break;
      case "Wednesday":
        dayNumber = 2;
        break;
      case "Thursday":
        dayNumber = 3;
        break;
      case "Friday":
        dayNumber = 4;
        break;
      case "Saturday":
        dayNumber = 5;
        break;
      case "Sunday":
        dayNumber = 6;
        break;

    }

    System.out.println("How many days into the future do you want to know the "
                      + "weekday?");
    int daysIntoFuture = input.nextInt();

      int calculateDay = (dayNumber + daysIntoFuture)%7;

      String resultDay = "";

      switch (calculateDay){
        case 0:
          resultDay = "Monday";
          break;
        case 1:
          resultDay = "Thuesday";
          break;
        case 2:
          resultDay = "Wednesday";
          break;
         case 3:
          resultDay = "Thursday";
          break;
        case 4:
          resultDay = "Friday";
          break;
        case 5:
          resultDay = "Saturday";
          break;
         case 6:
          resultDay = "Sunday";
          break;
        }

    System.out.print("After " + daysIntoFuture/7 + " weeks and "
              + daysIntoFuture%7 + " days" );

    System.out.println(", the day will be a "
                      + resultDay + "." );

    input.close();
  }
}
