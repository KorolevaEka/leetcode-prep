import java.util.List;

public class Solution {
    public interface Locator {
        String toCss();
    }

    public static class ById implements Locator {
        public ById(String id) {
            throw new UnsupportedOperationException("TODO");
        }

        public String toCss() {
            throw new UnsupportedOperationException("TODO");
        }
    }

    public static class ByClass implements Locator {
        public ByClass(String name) {
            throw new UnsupportedOperationException("TODO");
        }

        public String toCss() {
            throw new UnsupportedOperationException("TODO");
        }
    }

    public static class ByTag implements Locator {
        public ByTag(String tag) {
            throw new UnsupportedOperationException("TODO");
        }

        public String toCss() {
            throw new UnsupportedOperationException("TODO");
        }
    }

    public static class ByAttribute implements Locator {
        public ByAttribute(String name, String value) {
            throw new UnsupportedOperationException("TODO");
        }

        public String toCss() {
            throw new UnsupportedOperationException("TODO");
        }
    }

    public static String chain(List<Locator> path) {
        throw new UnsupportedOperationException("TODO");
    }
}
