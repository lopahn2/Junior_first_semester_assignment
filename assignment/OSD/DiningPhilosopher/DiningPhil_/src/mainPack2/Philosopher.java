package mainPack2;

public class Philosopher extends Thread {
	

	private int phId;
	private String[] stateSet = {"THINKING", "HUNGRY", "EATING"};
	private String state = "";
	private miscsubs misc = miscsubs.getInstance();
	public Philosopher(int phId) {
		this.phId = phId;
		this.state = stateSet[0];
		
	}
	
	@Override
	public void run() {
		miscsubs.RandomDelay();
		while(true) {
			if(state == stateSet[0]) {
				miscsubs.RandomDelay();
				state = stateSet[1];
			}
			if(state == stateSet[1]) {
				
				if(misc.pickChopstick(phId)) {
					state = stateSet[2];
				}
				
				
			}
			if(state == stateSet[2]) {
				

				miscsubs.RandomDelay();
				miscsubs.StartEating(phId);
				
				state = stateSet[0];
			}
		}
	}
	
	
}
