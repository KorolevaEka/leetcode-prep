public class Solution {
    public static String toFileName(String testName) {
        if (testName.isBlank()) {
            return "";
        }
        return String.join("_", testName.split("\\s+")).toLowerCase();
    }
}
