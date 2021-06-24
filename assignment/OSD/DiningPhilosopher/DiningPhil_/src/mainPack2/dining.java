// Use java threads to simulate the Dining Philosophers Problem
// YoungHwanPhan.  Programming assignment 2 (from ece.gatech.edu) */
package mainPack2;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;




class dining
{
    public static void main(String args[])
    {
        System.out.println("Starting the Dining Philosophers Simulation\n");
        miscsubs.InitializeChecking();
        // Your code here...
        
        ExecutorService pool = Executors.newCachedThreadPool();
        for(int i = 0 ; i<miscsubs.NUMBER_PHILOSOPHERS; i++) {
        	pool.execute(new Philosopher(i));
        }
        
        pool.shutdown();
        // End of your code
              
        miscsubs.LogResults();
        
    }
};


