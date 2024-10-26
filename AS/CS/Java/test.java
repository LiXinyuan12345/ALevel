import java.util.*;

public class test {
  public static void main(String[] args) 
  {
    String[]  ignoreWords={"the","and","of","to","for"};
    Scanner input = new Scanner(System.in);

    String   origin = input.nextLine();
    String[] words  = origin.split(" ");
    String   result ="";
    for (String word : words) {

        boolean matched = true;
        for (String igWord : ignoreWords)
        {
            if ( word.equalsIgnoreCase(igWord))
            {
                matched = false;    
                break;
            }
        }

        if (matched)
            result += word.charAt(0);
    }
    System.out.printf(result);
  }
}