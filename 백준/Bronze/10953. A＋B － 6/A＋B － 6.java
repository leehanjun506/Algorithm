
import java.util.*;
public class Main {
public static void main(String [] args) {
	Scanner scanner=new Scanner(System.in);
	int num=scanner.nextInt();
	int arr[]=new int[num];
	for(int i=0;i<num;i++) {
		String s=scanner.next();
		String arr1[]=s.split(",");
		arr[i]=Integer.parseInt(arr1[0])+Integer.parseInt(arr1[1]);
	}
	for(int i=0;i<num;i++) {
		System.out.println(arr[i]);
	}


scanner.close();
}
}