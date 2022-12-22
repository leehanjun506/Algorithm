import java.util.Scanner;
public class Main {
	 static int f(int x,int y) {
		if(x%y==0)
			return y;
		else
			return f(y,x%y);
	}
	static int l(int x,int y) {
		return x*y/f(x,y);
	}
public static void main(String [] args)  {
	Scanner sc=new Scanner(System.in);
	int a,b;
	int c,d;
	a=sc.nextInt();
	b=sc.nextInt();
	c=Math.max(a, b);
	d=Math.min(a, b);
	System.out.println(f(c,d));
	System.out.println(l(c,d));
}
}