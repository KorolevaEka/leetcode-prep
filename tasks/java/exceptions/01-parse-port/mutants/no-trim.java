public class Solution {
    public static int parsePort(String text) {
        if (text == null) {
            throw new IllegalArgumentException("port is null");
        }
        int port;
        try {
            port = Integer.parseInt(text);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("not a number: " + text, e);
        }
        if (port < 1 || port > 65535) {
            throw new IllegalArgumentException("out of range: " + port);
        }
        return port;
    }
}
