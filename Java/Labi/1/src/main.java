import java.util.Scanner;
public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float a, b, c, s;
		Scanner num = new Scanner(System.in);
		
		System.out.println("Вычисление объема параллелепипеда. ");
		System.out.println("Введите исходные данные:");
		System.out.print("Длина (см) ->");
		a = num.nextFloat();
		System.out.print("Ширина (см) ->");
		b = num.nextFloat();
		System.out.print("Высота (см) ->");
		c = num.nextFloat();
		
		s = a*b*c;
		System.out.print("Объем: "+s+" куб.см");
	}

}
