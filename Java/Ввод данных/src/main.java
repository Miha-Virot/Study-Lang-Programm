import java.util.Scanner;

public class main {

public static void main(String[] args) {
	// TODO Auto-generated method stub
	Scanner num =new Scanner(System.in);
	int i;
	i=num.nextInt();
	System.out.println("My variable is " +i);
	
	Scanner str =new Scanner(System.in);
	String symbols;
	symbols = str.nextLine();
	System.out.print("My variable is " +symbols);
}
}