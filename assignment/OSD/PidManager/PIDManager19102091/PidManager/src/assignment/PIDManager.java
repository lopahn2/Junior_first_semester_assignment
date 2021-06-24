package assignment;

public interface PIDManager {
	public static final int MIN_PID = 4;
	public static final int MAX_PID = 127;
	
	public int getPID();
	
	public int getPIDWait();
	
	public void releasePID(int pid);
}
