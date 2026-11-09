import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class Solution {
    public record TestRun(String name, String status, int durationMs) {}

    public static Map<String, Long> failedByModule(List<TestRun> runs) {
        return runs.stream()
                .collect(Collectors.groupingBy(r -> module(r.name()), TreeMap::new, Collectors.counting()));
    }

    private static String module(String name) {
        int dot = name.indexOf('.');
        return dot < 0 ? name : name.substring(0, dot);
    }
}
