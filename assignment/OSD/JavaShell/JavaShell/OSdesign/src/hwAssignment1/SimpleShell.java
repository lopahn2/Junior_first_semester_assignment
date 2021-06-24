package hwAssignment1;
import java.io.*;
import java.util.ArrayList;
import java.util.List;


public class SimpleShell {
	
	
	public static void main(String[] args) throws java.io.IOException{
		String commandLine;
		BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
		List<String> cmdlist = new ArrayList<String>();
		ProcessBuilder pb = new ProcessBuilder();
		File startDir = new File(System.getProperty("user.dir"));
		pb.directory(startDir);
		
		int index = 0;
		
		//we break out with <control><c>
		while(true) {
			//read what the user entered
			System.out.print("jsh>");
			commandLine = console.readLine();
			String[] cmds = commandLine.split(" ");
			
			
			
			
			
			
			//if the user entered a return, just loop again
			if(commandLine.equals("")) {
				continue;
			}
			
			
			
			if(commandLine.equals("exit")||commandLine.equals("quit")) {
				System.out.println("Goodbye");
				System.exit(0);
			}
			
			
			
			
			try {
				
				
		
				
				
				int size = cmds.length;
				
				
				if(cmds[0].equals("history!!")) {
					//Because Linux did not show !! when we type history command
					
				}else if(cmds[0].matches("history!\\d+")) {
					//Because Linux did not show !<integer> when we type history command
					
				}else if(size>1) {
					String temp = "";
					for(int i = 0; i<size; i++) {
						temp += cmds[i]+" ";
						
					}
					String tempCmd = temp.substring(0,temp.length()-1);
					cmdlist.add(tempCmd);
					System.out.println(cmdlist);
					index++;
				}else {
					cmdlist.add(cmds[0]);
					System.out.println(cmdlist);
					index++;
				}
				
				
				
				
				
				
				if(commandLine.contains("history")) {
					
					
					if(commandLine.equals("history")) {
						int i = 0;
						for (String s: cmdlist){
							
							System.out.println((i++) + " " + s);
						}
						continue;
					}
					
					if(commandLine.substring(("history").length()).equals("!!")) {
						if (cmdlist.size() == 0){
							System.out.println("You have not initiate program");
							continue;
						}
						else {
							String newcmds = cmdlist.get(cmdlist.size()-1);
							if(newcmds.equals("history")) {
								int i = 0;
								for (String s: cmdlist){
									
									System.out.println((i++) + " " + s);
								}
								continue;
							}
							cmds = newcmds.split(" ");
							commandLine = newcmds;
						}
					}else if(commandLine.substring(("history").length()+1).matches("\\d+")){
						Integer targetIndex = Integer.parseInt(commandLine.substring(("history").length()+1));
						if (targetIndex > index){
							System.out.println("Outbounded Error");
							System.out.println("Please input valid number");
							continue;
						}
						String newcmds = cmdlist.get(targetIndex);
						if(newcmds.equals("history")) {
							int i = 0;
							for (String s: cmdlist){
								
								System.out.println((i++) + " " + s);
							}
							continue;
						}
						cmds = newcmds.split(" ");
						commandLine = newcmds;
						
					}
					
				}
					

				
				
				
				if (commandLine.contains("cd")){
					
					
					if (commandLine.equals("cd")){
						File home = new File(System.getProperty("user.home"));
						System.out.println(home);
						pb.directory(home);
						continue;
						
						
					}else if (commandLine.equals("cd ..")){
						File parentDir = new File(pb.directory().getParent());
						System.out.println(parentDir);
						pb.directory(parentDir);
						continue;
						
					}else{
						String dir = cmds[1];
						File newDir = new File(pb.directory() + File.separator + dir);
						if (newDir.isDirectory()){
							System.out.println(newDir);
							pb.directory(newDir);
							continue;
							
						}else {
							System.out.println(dir + ": No such file or directory");
							continue;
						}
					}
				}
				
				
				
				
				
				
				
				pb.command(cmds);
				
				
				Process process = pb.start();
				
				InputStream is = process.getInputStream();
				InputStreamReader isr = new InputStreamReader(is);
				BufferedReader br = new BufferedReader(isr);
				
				String line;
				while((line=br.readLine()) != null) {
					System.out.println(line);
					
				}
				
				br.close();
			}catch(Exception e) {
				System.out.println(e);
			}
			
			
			
			
			
		}

	}

}
