package assignment;

import java.util.Random;


public class MyThread extends Thread {
	private String threadName;
	private int createTime;
	private int threadTime;
	private int processTime;
	
	private int pid;
	private int getPIDType;
	private Thread runningThreadasProcess;
	private Random random = new Random();
	private PIDManagerClass pidM = PIDManagerClass.getInstance();
	
	public MyThread(String threadName, int threadTime,int processTime, int getPIDType) {
		this.threadName = threadName;
		this.threadTime = threadTime;
		this.processTime = processTime;
		
		this.getPIDType = getPIDType;
		this.runningThreadasProcess = new Thread(this, this.threadName);

		runningThreadasProcess.start();
	}
	@Override
    public void run() {
		getPIDtype(this.getPIDType);
		
	}
	
	public void getPIDtype(int gettype) {
		if(gettype == 0) {
			try {
				
				createTime = random.nextInt(processTime*1000);
				Thread.sleep(createTime);
				this.pid= pidM.getPID();
				if(this.pid !=-1) {
					
					System.out.println(threadName+" created at "+createTime+"ms "+"pid: "+this.pid);
					
					
				}else {
					//if getPID() return -1, this thread is covered under else part by return;
				}
			}catch(Exception e) {
				System.err.println(e);
			}
			
			try {
				
				if((createTime+threadTime*1000) > processTime*1000) {
					Thread.sleep(threadTime*1000);
					System.out.println(processTime+"sec passed... Program ends");
					System.exit(0);
				}else {
					if(this.pid == -1) {
						System.out.println("All pid are used now.");
						System.out.println("this thread can not get pid.");
						return;
					}
					Thread.sleep(threadTime*1000);
					pidM.releasePID(this.pid);
					System.out.println(threadName+" destroyed at "+(createTime+threadTime*1000)+"ms"+" pid: "+this.pid );
				}
			}catch(Exception e) {
				System.err.println(e);
			}
		}else {
			try {
				
				createTime = random.nextInt(processTime*1000);
				Thread.sleep(createTime);
				this.pid= pidM.getPIDWait();
				if(this.pid !=-1) {
					
					System.out.println(threadName+" created at "+createTime+"ms "+"pid: "+this.pid);
					
					
				}else {
					//getPIDWait() cover this part.
				}

			}catch(Exception e) {
				System.err.println(e);
			}
			
			try {
				
				if((createTime+threadTime*1000) > processTime*1000) {
					Thread.sleep(threadTime*1000);
					System.out.println(processTime+" sec passed... Program ends");
					System.exit(0);
				}else {
					Thread.sleep(threadTime*1000);
					pidM.releasePID(this.pid);
					System.out.println(threadName+" destroyed at "+(createTime+threadTime*1000)+"ms"+"pid: "+this.pid );
				}
			}catch(Exception e) {
				System.err.println(e);
			}
		}
		
	}
	
	
	
}
