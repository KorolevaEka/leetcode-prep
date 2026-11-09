import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

public class Solution {
    public static List<String> runOrder(Map<String, List<String>> dependsOn) {
        Map<String, Integer> waiting = new HashMap<>();
        Map<String, List<String>> dependents = new HashMap<>();
        for (Map.Entry<String, List<String>> entry : dependsOn.entrySet()) {
            String task = entry.getKey();
            waiting.putIfAbsent(task, 0);
            for (String dep : entry.getValue()) {
                waiting.merge(task, 1, Integer::sum);
                dependents.computeIfAbsent(dep, k -> new ArrayList<>()).add(task);
            }
        }
        TreeSet<String> ready = new TreeSet<>();
        for (Map.Entry<String, Integer> entry : waiting.entrySet()) {
            if (entry.getValue() == 0) {
                ready.add(entry.getKey());
            }
        }
        List<String> order = new ArrayList<>();
        while (!ready.isEmpty()) {
            String next = ready.pollFirst();
            order.add(next);
            for (String dependent : dependents.getOrDefault(next, List.of())) {
                if (waiting.merge(dependent, -1, Integer::sum) == 0) {
                    ready.add(dependent);
                }
            }
        }
        if (order.size() < waiting.size()) {
            throw new IllegalStateException("cycle in dependencies");
        }
        return order;
    }
}
