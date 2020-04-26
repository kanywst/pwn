import java.util.*;

public class fragile
{
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter flag: ");
        String userInput = scanner.next();
        String input = userInput.substring("rtcp{".length(),userInput.length()-1);
        check_reverse();
        if (check(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }
    
    public static boolean check(String input){
        boolean h = false;
        String flag = "h1_th3r3_1ts_m3";
        String theflag = "";
        if(input.length() != flag.length()){
            return false;
        }
        for(int i = 0; i < flag.length(); i++){
            theflag += (char)((int)(flag.charAt(i)) + (int)(input.charAt(i)));
        }
        return theflag.equals("ÐdØÓ§åÍaèÒÁ¡");
    }

    public static void check_reverse(){
    	String flag = "h1_th3r3_1ts_m3";
    	String answer = "ÐdØÓ§åÍaèÒÁ¡";
    	String theflag = "";

    	for(int i = 0; i< flag.length();i++){
    		theflag += (char)((int)(answer.charAt(i)) - (int)(flag.charAt(i)));
    	}

    	System.out.println(theflag);
    }
}
