import java.util.*;

public class Main {
	static int mid;
	static int c;
	static int mid(int a,int b) {
		if(a>=b) {
			mid=b;
			c=2*b-a;
			return c;
		}
		else {
			mid=a;
			c=2*a-b;
			return c;
		}
	}
	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		while(true) {
		int a=scanner.nextInt();
		int b=scanner.nextInt();
		if(a==0&&b==0)
			break;
		System.out.println(mid(a,b));
	}
}
}