import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("пример из условия")
    void example() {
        Solution.LruCache<String, Integer> cache = new Solution.LruCache<>(2);
        cache.put("a", 1);
        cache.put("b", 2);
        cache.get("a");
        cache.put("c", 3);
        assertNull(cache.get("b"));
        assertEquals(1, cache.get("a"));
        assertEquals(3, cache.get("c"));
        assertEquals(2, cache.size());
    }

    @Test
    @DisplayName("без чтений вытесняется самая старая запись")
    void evictsOldest() {
        Solution.LruCache<String, Integer> cache = new Solution.LruCache<>(2);
        cache.put("a", 1);
        cache.put("b", 2);
        cache.put("c", 3);
        assertNull(cache.get("a"));
        assertEquals(2, cache.get("b"));
        assertEquals(3, cache.get("c"));
    }

    @Test
    @DisplayName("обновление значения освежает ключ")
    void updateRefreshes() {
        Solution.LruCache<String, Integer> cache = new Solution.LruCache<>(2);
        cache.put("a", 1);
        cache.put("b", 2);
        cache.put("a", 10);
        cache.put("c", 3);
        assertNull(cache.get("b"));
        assertEquals(10, cache.get("a"));
        assertEquals(2, cache.size());
    }

    @Test
    @DisplayName("отсутствующий ключ и размер")
    void missingAndSize() {
        Solution.LruCache<String, Integer> cache = new Solution.LruCache<>(3);
        assertNull(cache.get("x"));
        assertEquals(0, cache.size());
        cache.put("x", 1);
        cache.put("y", 2);
        assertEquals(2, cache.size());
    }

    @Test
    @DisplayName("ёмкость 1")
    void capacityOne() {
        Solution.LruCache<String, Integer> cache = new Solution.LruCache<>(1);
        cache.put("a", 1);
        cache.put("b", 2);
        assertNull(cache.get("a"));
        assertEquals(2, cache.get("b"));
        assertEquals(1, cache.size());
    }

    @Test
    @DisplayName("ёмкость заполняется полностью")
    void fillsUpToCapacity() {
        Solution.LruCache<Integer, String> cache = new Solution.LruCache<>(3);
        cache.put(1, "one");
        cache.put(2, "two");
        cache.put(3, "three");
        assertEquals(3, cache.size());
        assertEquals("one", cache.get(1));
        assertEquals("two", cache.get(2));
        assertEquals("three", cache.get(3));
    }

    @Test
    @DisplayName("неверная ёмкость: IllegalArgumentException")
    void badCapacity() {
        assertThrows(IllegalArgumentException.class, () -> new Solution.LruCache<String, Integer>(0));
        assertThrows(IllegalArgumentException.class, () -> new Solution.LruCache<String, Integer>(-3));
    }
}
