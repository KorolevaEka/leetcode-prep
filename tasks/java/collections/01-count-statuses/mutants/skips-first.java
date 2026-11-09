import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static Map<String, Integer> countStatuses(List<String> statuses) {
        Map<String, Integer> counts = new HashMap<>();
        for (String status : statuses) {
            counts.put(status, counts.getOrDefault(status, -1) + 1);
        }
        return counts;
    }
}
