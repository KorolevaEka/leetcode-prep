import java.util.LinkedHashMap;

public class Solution {
    public static class LruCache<K, V> {
        private final int capacity;
        private final LinkedHashMap<K, V> entries = new LinkedHashMap<>();

        public LruCache(int capacity) {
            if (capacity < 1) {
                throw new IllegalArgumentException("capacity must be positive");
            }
            this.capacity = capacity;
        }

        public V get(K key) {
            if (!entries.containsKey(key)) {
                return null;
            }
            return entries.get(key);
        }

        public void put(K key, V value) {
            entries.remove(key);
            entries.put(key, value);
            if (entries.size() > capacity) {
                K eldest = entries.keySet().iterator().next();
                entries.remove(eldest);
            }
        }

        public int size() {
            return entries.size();
        }
    }
}
