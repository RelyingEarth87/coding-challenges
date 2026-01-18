import java.util.ArrayList;
import java.util.Arrays;

/**
 * Defines a static method to determine someone's recommended bed time based on their alarm time and sleep duration.
 * Created based on a coding challenge given on <a href="https://slothbytes.beehiiv.com/">SlothBytes</a>
 * 
 * @author RelyingEarth87
 * 
 */
public class BedTime {
	
	/**
	 * Returns a bed time to give a person the required amount of sleep for their wake up time.
	 * All times are in 24 Hour time.
	 * @param times a number of times in [HH:MM, HH:MM] format where the first is the time the 
	 * alarm will go off and the second is the required amount of sleep
	 * @return the necessary bed times to achieve the required amount of sleep (in HH:MM)
	 */
	public static ArrayList<String> bedTime(String[][] times) {
		ArrayList<String> bedtimes = new ArrayList<>();
		
		for (String[] time : times) {
			String alarmTime = time[0];
			String sleepDuration = time[1];
			
			String[] alarmTimes = alarmTime.strip().split(":");
			String[] sleepDurTimes = sleepDuration.strip().split(":");

			int hoursDiff = Integer.parseInt(alarmTimes[0]) - Integer.parseInt(sleepDurTimes[0]);
			int minsDiff = Integer.parseInt(alarmTimes[1]) - Integer.parseInt(sleepDurTimes[1]);
			
			if (minsDiff < 0) {
				hoursDiff -= 1;
			}
			
			String hours = String.valueOf((hoursDiff + 24) % 24);
			String minutes =  String.valueOf((minsDiff + 60) % 60);
			
			if (hours.length() < 2) {
				hours = "0" + hours;
			}
			
			if (minutes.length() < 2) {
				minutes = "0" + minutes;
			}
			
			
			bedtimes.add(hours + ":" + minutes);
		}
		
		return bedtimes;
	}
	
	/**
	 * Runs validation tests for {@link BedTime#bedTime(String[][])} method
	 * @param args not implemented
	 */
	public static void main(String[] args) {
		String[][][] inputs = {{{"07:50", "07:50"}}, {{"06:15", "10:00"}, {"08:00", "10:00"}, {"09:30", "10:00"}}, 
				{{"05:45", "04:00"}, {"07:10", "04:30"}}};
		ArrayList<String[]> outputs = new ArrayList<>(){{
			add(new String[] {"00:00"}); 
			add(new String[]{"20:15", "22:00", "23:30"});
			add(new String[]{"01:45", "02:40"});
			}};
		
		ArrayList<String> output;
		
		for (int i = 0; i < inputs.length; i++) {
			output = bedTime(inputs[i]);
			
			for (int j = 0; j < output.size(); j++) {
				try {
					assert output.get(j).equals(outputs.get(i)[j]);
				} catch (AssertionError ae) {
					System.out.println("Test " + i + "has gone wrong. Time number " + j);
				}
			}
			
			System.out.println("bedTime(" + Arrays.deepToString(inputs[i]) + ")");
			System.out.println("output = " + output);
			System.out.println();
			
			
		}
		
	}
}
