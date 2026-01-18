import java.util.Arrays;

/**
 * Defines a static method to determine how many numbers are missing in an integer array
 * Created based on a coding challenge given on <a href="https://slothbytes.beehiiv.com/">SlothBytes</a>
 * 
 * @author RelyingEarth87
 */
public class HowManyMissing {
	
	/**
	 * Determines how many numbers are missing from an integer array
	 * @param nums an integer array that may or may not have missing numbers
	 * @return number of sequential items missing from array
	 */
	public static int howManyMissing(int[] nums) {
		// clones and sorts so array stays the same
		int[] nums1 = nums.clone();
		Arrays.sort(nums1);
		
		int total = 0;
		
		for (int i = 0; i < nums1.length - 1; i++) {
			total += nums1[i+1] - nums1[i] - 1;
		}
		
		return total;
	}
	
	/**
	 * Runs validation tests for {@link HowManyMissing#howManyMissing(int[])}
	 * @param args not implemented
	 */
	public static void main(String[] args) {
		int[][] inputs = {{1, 2, 3, 8, 9}, {1, 3}, {7, 10, 11, 12}, {1, 3, 5, 7, 9, 11}, {5, 6, 7, 8}, {9, 8, 3, 2, 1}, {}};
		int[] outputs = {4, 1, 2, 5, 0, 4, 0};
		
		int output;
		
		for (int i = 0; i < inputs.length; i++) {
			output = howManyMissing(inputs[i]);
			
			assert output == outputs[i];
			
			System.out.println("howManyMissing(" + Arrays.toString(inputs[i]) + ")");
			System.out.println("output = " + output);
			System.out.println();
		}

	}

}
