public class Solution {
    public static String shortenMiddle(String s, int max) {
        if (max < 3) {
            throw new IllegalArgumentException("max must be at least 3");
        }
        if (s.length() <= max) {
            return s;
        }
        int keep = max - 2;
        int head = (keep + 1) / 2;
        int tail = keep / 2;
        return new StringBuilder()
                .append(s, 0, head)
                .append("...")
                .append(s, s.length() - tail, s.length())
                .toString();
    }
}
