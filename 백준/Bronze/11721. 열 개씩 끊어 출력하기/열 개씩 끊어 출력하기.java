import java.util.*;
public class Main {
public static void main(String [] args) {
	Scanner scanner=new Scanner(System.in);
	String str=scanner.nextLine();
	for(int i=0;i<str.length();i+=10) {
		try{
			System.out.println(str.substring(i,i+10));
		}
		catch(StringIndexOutOfBoundsException e) {
			System.out.println(str.substring(i));
		}
	}
}
}