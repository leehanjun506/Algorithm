import java.util.*;
public class Main {
public static void main(String [] args) {
	Scanner scanner=new Scanner(System.in);
	int x=1,y=1;
	int month_day=0;
	int month=scanner.nextInt();
	int day=scanner.nextInt();
	
	switch(month) {
	case 1:
		month_day=0;
		break;
	case 2:
		month_day=31;
		break;
	case 3:
		month_day=31+28;
		break;
	case 4:
		month_day=31+28+31;
		break;
	case 5:
		month_day=31+28+31+30;
		break;
	case 6:
		month_day=31+28+31+30+31;
		break;
	case 7:
		month_day=31+28+31+30+31+30;
		break;
	case 8:
		month_day=31+28+31+30+31+30+31;
		break;
	case 9:
		month_day=31+28+31+30+31+30+31+31;
		break;
	case 10:
		month_day=31+28+31+30+31+30+31+31+30;
		break;
	case 11:
		month_day=31+28+31+30+31+30+31+31+30+31;
		break;
	case 12:
		month_day=31+28+31+30+31+30+31+31+30+31+30;
		break;
	}
	int sum=month_day+day;
	
	switch((sum-1)%7) {
	case 0:
		System.out.print("MON");
		break;
	case 1:
		System.out.print("TUE");
		break;
	case 2:
		System.out.print("WED");
		break;
	case 3:
		System.out.print("THU");
		break;
	case 4:
		System.out.print("FRI");
		break;
	case 5:
		System.out.print("SAT");
		break;
	case 6:
		System.out.print("SUN");
		break;
	}
	scanner.close();
}
}