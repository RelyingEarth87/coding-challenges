
public class DayOfYear {
	
	public static int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	/**
	 * Determines what number day a date is in the given year
	 * @param dateTime a date in mm/dd/yy format
	 * @return the number day (out of 365 or 366 for leap years) corresponding to the date
	 */
	public static int dayOfYear(String dateTime) {
		String[] date = dateTime.strip().split("/");
		int month = Integer.parseInt(date[0]);
		int day = Integer.parseInt(date[1]);
		int year = Integer.parseInt(date[2]);
		
		boolean isLeapYear = checkLeapYear(year);
		
		int daySum = 0;
		int i = 1;
		while (i < month) {
			daySum += days[i-1];
			i++;
		}
		
		daySum += day;
		
		if (month > 2 && isLeapYear) {
			return daySum + 1;
		}
		
		return daySum;
	}
	
	/**
	 * Determines whether or not a given year is a leap year
	 * @param year a year in the Gregorian Calendar
	 * @return true if year is a leap year; false otherwise
	 */
	public static boolean checkLeapYear(int year) {
		if (year % 4 == 0) {
			if (year % 100 == 0) {
				return year % 400 == 0;
			}
			return true;
		}
		return false;
	}

	/**
	 * Runs validation tests for {@link DayOfYear#dayOfYear(String)} method
	 * @param args not implemented
	 */
	public static void main(String[] args) {
		String[] inputs = {"12/13/2020", "11/16/2020", "1/9/2019", "3/1/2004", "12/31/2000", "12/31/2019"};
		int[] outputs = {348, 321, 9, 61, 366, 365};
		
		int output;
		
		for (int i = 0; i < inputs.length; i++) {
			output = dayOfYear(inputs[i]);
			
			assert output == outputs[i];
			
			System.out.println("dayOfYear(\"" + inputs[i] + "\")");
			System.out.println("output = " + output);
			System.out.println();
		}

	}

}
