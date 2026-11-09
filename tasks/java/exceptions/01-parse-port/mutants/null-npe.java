public class Solution {
    public static int parsePort(String text) {
        int port;
        try {
            port = Integer.parseInt(text.trim());
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("not a number: " + text, e);
        }
        if (port < 1 || port > 65535) {
            throw new IllegalArgumentException("out of range: " + port);
        }
        return port;
    }
}
