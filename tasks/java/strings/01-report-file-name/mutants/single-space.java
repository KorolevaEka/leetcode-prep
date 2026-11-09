public class Solution {
    public static String toFileName(String testName) {
        String trimmed = testName.trim();
        if (trimmed.isEmpty()) {
            return "";
        }
        return String.join("_", trimmed.split(" ")).toLowerCase();
    }
}
