public class Solution {
    public static String formatSize(long bytes) {
        if (bytes < 0) {
            throw new IllegalArgumentException("bytes must not be negative");
        }
        if (bytes < 1024) {
            return bytes + " B";
        }
        String[] units = {"KB", "MB"};
        long divisor = 1024;
        int unit = 0;
        while (unit < units.length - 1 && bytes >= divisor * 1024) {
            divisor *= 1024;
            unit++;
        }
        long tenths = bytes * 10 / divisor;
        return tenths / 10 + "." + tenths % 10 + " " + units[unit];
    }
}
