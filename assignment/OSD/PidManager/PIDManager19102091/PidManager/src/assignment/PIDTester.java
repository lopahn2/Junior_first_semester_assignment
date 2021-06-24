package assignment;

import java.util.Scanner;


public class PIDTester {
	
	public static void main(String[] args) {
		PIDManagerClass pidM = PIDManagerClass.getInstance();
		Scanner scan = new Scanner(System.in);
		System.out.println("--------------ITM-19102091-YoungHwan-Phan---------------");
		System.out.println("--------------------------------------------------------");
		System.out.println("--------------INPUT-POSTIVE-INTEGER-NUMBER--------------");
		System.out.println("--------------------------------------------------------");
		System.out.println("----------ProcessNum, ProcessTime, ProgramTime----------");
		try {
			int ThreadNum = scan.nextInt();
			int ThreadTime = scan.nextInt();
			int ProcessTime = scan.nextInt();
			if(ThreadNum<0||ThreadTime<0||ProcessTime <0) {
				System.out.println("<<<<Please input 'POSITIVE' 'INTEGER' number>>>>");
				System.out.println("<<<<Restart Program please>>>>");
				System.exit(0);
			}
			System.out.println("-----Select Mode : 0.getPID(), OtherNum.getPIDWait()------");
			int pidMode = scan.nextInt();
			pidM.setPIDManager(ThreadNum, ThreadTime, ProcessTime, pidMode);
		}catch(Exception e) {
			System.out.println("<<<<Please input 'POSITIVE' 'INTEGER' number>>>>");
			System.out.println("<<<<Restart Program please>>>>");
		}finally {
			scan.close();
		}
		
		
		

	}
	
	

}

