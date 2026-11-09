import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static class ConfigException extends Exception {
        public ConfigException(String message) {
            super(message);
        }
    }

    public static Map<String, String> parseConfig(List<String> lines) throws ConfigException {
        Map<String, String> config = new LinkedHashMap<>();
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i).trim();
            if (line.isEmpty() || line.startsWith("#")) {
                continue;
            }
            int eq = line.indexOf('=');
            if (eq < 0) {
                throw new ConfigException("line " + (i + 1));
            }
            String key = line.substring(0, eq).trim();
            String value = line.substring(eq + 1).trim();
            if (key.isEmpty() || config.containsKey(key)) {
                throw new ConfigException("line " + (i + 1));
            }
            config.put(key, value);
        }
        return config;
    }
}
