import java.util.Scanner;
public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float a, b, c, s;
		Scanner num = new Scanner(System.in);
		
		System.out.println("���������� ������ ���������������. ");
		System.out.println("������� �������� ������:");
		System.out.print("����� (��) ->");
		a = num.nextFloat();
		System.out.print("������ (��) ->");
		b = num.nextFloat();
		System.out.print("������ (��) ->");
		c = num.nextFloat();
		
		s = a*b*c;
		System.out.print("�����: "+s+" ���.��");
	}

}
