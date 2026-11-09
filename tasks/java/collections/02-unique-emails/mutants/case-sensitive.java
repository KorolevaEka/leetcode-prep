import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public static List<String> uniqueEmails(List<String> emails) {
        Set<String> seen = new HashSet<>();
        List<String> result = new ArrayList<>();
        for (String email : emails) {
            if (seen.add(email)) {
                result.add(email);
            }
        }
        return result;
    }
}
