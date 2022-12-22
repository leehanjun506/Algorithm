
import java.util.*;
public class Main {
public static void main(String [] args) {
	Scanner scanner=new Scanner(System.in);
	int num=scanner.nextInt();
	scanner.nextLine();
	String str=scanner.nextLine();
	int sum=0;
	int arr[]=new int[num];
	for(int i=0;i<num;i++) {
		if(i==num-1)
			arr[i]=Integer.parseInt(str.substring(i));
		else
			arr[i]=Integer.parseInt(str.substring(i,i+1));
		sum+=arr[i];
	}
	System.out.println(sum);
}
}