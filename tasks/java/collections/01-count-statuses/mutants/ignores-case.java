import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static Map<String, Integer> countStatuses(List<String> statuses) {
        Map<String, Integer> counts = new HashMap<>();
        for (String status : statuses) {
            counts.merge(status.toUpperCase(), 1, Integer::sum);
        }
        return counts;
    }
}
