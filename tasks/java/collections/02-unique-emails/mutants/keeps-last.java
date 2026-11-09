import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public static List<String> uniqueEmails(List<String> emails) {
        Set<String> seen = new HashSet<>();
        List<String> result = new ArrayList<>();
        for (String email : emails) {
            String key = email.toLowerCase();
            result.removeIf(x -> x.toLowerCase().equals(key));
            result.add(email);
        }
        return result;
    }
}
