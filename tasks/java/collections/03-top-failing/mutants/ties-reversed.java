import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static List<String> topFailing(List<String> failedNames, int n) {
        if (n <= 0) {
            return new ArrayList<>();
        }
        Map<String, Integer> counts = new HashMap<>();
        for (String name : failedNames) {
            counts.merge(name, 1, Integer::sum);
        }
        List<String> names = new ArrayList<>(counts.keySet());
        names.sort((a, b) -> {
            int byCount = Integer.compare(counts.get(b), counts.get(a));
            return byCount != 0 ? byCount : b.compareTo(a);
        });
        return new ArrayList<>(names.subList(0, Math.min(n, names.size())));
    }
}
