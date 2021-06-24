package assignment;


import java.util.Vector;


public class PIDManagerClass implements PIDManager {
	private static boolean flag = true;
	private static PIDManagerClass instance = new PIDManagerClass();
	private Vector<Integer> pids = new Vector<>();
	
	private PIDManagerClass() {
		
	}
	
	public static PIDManagerClass getInstance() {
		return instance;
	}
	
	public int setPIDManager(int threadNum, int threadTime, int processTime, int getPIDType) {
		System.out.println("----------------PID MANAGER SET----------------");
		
		for(int i = MIN_PID; i <= MAX_PID; i++) {
			pids.add(i);
			
		}
		for(int i = 0; i <= threadNum; i++) {
			
			
			new MyThread(("thread"+(i)),threadTime,processTime, getPIDType);
		}

		return 1;
	}
	

	
	
	
	@Override
	public int getPID() {
		if(pids.isEmpty()) {
			return -1;
		}else {
			int pd = pids.get(0);
			pids.remove(0);
			return pd;
		}
		
	}

	@Override
	public int getPIDWait() {	
		while(!flag) {
			//waiting
		}
		flag = false;
		//Critical Section
		int pidchild = getPID();
		while(pidchild==-1) {
			System.out.println("wait...");
			try {
				Thread.sleep(500);
			}catch(Exception e) {
				
			}
			pidchild= getPID();
			
		}
		flag = true;
		return pidchild;
	}

	@Override
	public void releasePID(int pid) {
		try {
        	pids.add(pid);
        	
        }catch(IllegalArgumentException e) {
        	System.err.println(e);
        }
		
	}

}
