import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<Integer> findAll(String text, String pattern) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i + pattern.length() <= text.length(); i++) {
            if (text.startsWith(pattern, i)) {
                result.add(i);
            }
        }
        return result;
    }
}
