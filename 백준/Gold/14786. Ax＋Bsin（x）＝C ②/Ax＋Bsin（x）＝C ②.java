import java.util.*;
public class Main {
	public static void main(String[] args) {
	Scanner scanner=new Scanner(System.in);
	double a=scanner.nextFloat();
	double b=scanner.nextFloat();
	double c=scanner.nextFloat();
	double low=0;
	double high=100000;
	double mid=(low+high)/2;
	double ans=0;
	while(true) {
	if((a*mid+b*Math.sin(mid)>c*(1-Math.pow(10, -10)))&&((a*mid+b*Math.sin(mid))<c*(1+Math.pow(10, -10)))) {
		ans=mid;
		break;
		}
	else if(a*mid+b*Math.sin(mid)<c) {
		low=mid;
		mid=(low+high)/2;
	}
	else {
		high=mid;
		mid=(low+high)/2;
	}
		
	}
	System.out.print(ans);
	}
}
