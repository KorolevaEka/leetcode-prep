import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public interface Locator {
        String toCss();
    }

    public static class ById implements Locator {
        private final String id;

        public ById(String id) {
            this.id = id;
        }

        public String toCss() {
            return "#" + id;
        }
    }

    public static class ByClass implements Locator {
        private final String name;

        public ByClass(String name) {
            this.name = name;
        }

        public String toCss() {
            return "." + name;
        }
    }

    public static class ByTag implements Locator {
        private final String tag;

        public ByTag(String tag) {
            this.tag = tag;
        }

        public String toCss() {
            return tag;
        }
    }

    public static class ByAttribute implements Locator {
        private final String name;
        private final String value;

        public ByAttribute(String name, String value) {
            this.name = name;
            this.value = value;
        }

        public String toCss() {
            return "[" + name + "=\"" + value + "\"]";
        }
    }

    public static String chain(List<Locator> path) {
        return path.stream().map(Locator::toCss).collect(Collectors.joining(" "));
    }
}
