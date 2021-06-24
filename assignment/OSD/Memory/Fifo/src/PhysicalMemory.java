/**
 * Class to emulate the physical memory
 */
public class PhysicalMemory{
    /**
     * variable to emulate frames in memory
     */
    Frame[] frames;
    /**
     * we need a variable to store how many
     * frames are used
     */
    int currentFreeFrame;
    
    int replacement = 0;

    /**
     * Constructor
     */
    public PhysicalMemory(){
        this.frames = new Frame[128];
        this.currentFreeFrame = 0;
    }


    /**
     * function to add a new frame to memory
     *
     * @param f Frame to be added
     * @return int the frame number just added
     */
    public int addFrame(Frame f){
    		if(this.currentFreeFrame > 127) {
    			StateController.isfull =true;
    			
    			for(int i = 0 ; i < 127; i++) {
    				this.frames[i] = this.frames[i+1];
    			}
    			this.frames[this.currentFreeFrame-1]= new Frame(f.data);
    			StateController.targetlist.add(this.currentFreeFrame);
    			replacement++;
    			return this.currentFreeFrame-1;
    		}
    		StateController.isfull = false;
    		this.frames[this.currentFreeFrame] = new Frame(f.data);
    		StateController.targetlist.add(this.currentFreeFrame);
            this.currentFreeFrame++;
            return this.currentFreeFrame-1;
    	
        
    }


    /**
     * function to get value in memory
     *
     * @param f_num int frame number
     * @param offset int offset
     * @return int content in specified location
     */
    public int getValue(int f_num, int offset){
        Frame frame = this.frames[f_num];
        return frame.data[offset];
    }


}


/**
 * wrapper class to group all frame related logics
 */
class Frame {
    /**
     * variable to store datas of this frame
     */
    int[] data;


    /**
     * Constructor
     *
     * @param d int[256] for initializing frame
     */
    public Frame(int[] d){
        this.data = new int[256];
        for(int i=0;i<256;i++){
            this.data[i] = d[i];
        }
    }


    /**
     * Copy Constructor
     *
     * @param f Frame to be copied
     */
    public Frame(Frame f){
        this.data = new int[256];
        System.arraycopy(f.data, 0, this.data, 0, 256);
    }
}

