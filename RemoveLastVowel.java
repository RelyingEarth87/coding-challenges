/**
 * A class that takes a sentence and removes the last vowel from every word
 * 
 * Created based on a challenge given from <a href="https://slothbytes.beehiiv.com/">SlothBytes<a>
 * 
 * @author RelyingEarth87
 */
public class RemoveLastVowel {

	public static String vowels = "AEIOUaeiou";
	
	/**
	 * Takes a String and removes the last vowel present in every word
	 * @param input a String representing a sentence
	 * @return the same String, with the last vowel in each word removed
	 */
	public static String removeLastVowel(String input) {
		String[] words = input.strip().split(" ");

		word_loop: for (int i = 0; i < words.length; i++) {
			for (int j = words[i].length() - 1; j >= 0; j--) {
				if (vowels.contains(String.valueOf(words[i].charAt(j))) && j > 0) {
					words[i] = words[i].substring(0, j) + words[i].substring(j + 1, words[i].length());
					continue word_loop;
				} else if (vowels.contains(String.valueOf(words[i].charAt(j)))) {
					words[i] = words[i].substring(j + 1, words[i].length());
					continue word_loop;
				}
			}
		}

		return String.join(" ", words);
	}
	
	/**
	 * Runs validation tests for {@link RemoveLastVowel#removeLastVowel(String)} method
	 * @param args not implemented
	 */
	public static void main(String[] args) {
		String output;

		String[] inputs = { "Those who dare to fail miserably can achieve greatly.",
				"Love is a serious mental disease.", "Get busy living or get busy dying.",
				"If you want to live a happy life, tie it to a goal, not to people." };

		String[] outputs = { "Thos wh dar t fal miserbly cn achiev gretly.", "Lov s  serios mentl diseas.",
				"Gt bsy livng r gt bsy dyng.", "f yo wnt t liv  hppy lif, ti t t  gol, nt t peopl." };

		for (int i = 0; i < inputs.length; i++) {
			output = removeLastVowel(inputs[i]);

			try {
				assert outputs[i].equals(output);
			} catch (AssertionError ae) {
				System.out.println("Test " + i + " has failed");
			}

			System.out.println("removeLastVowel(\"" + inputs[i] + "\")");
			System.out.println("output = \"" + output + "\"");
			System.out.println();
		}

	}

}
