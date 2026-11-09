import java.util.HashSet;
import java.util.Set;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("сложение даёт новый объект")
    void plusReturnsNew() {
        Solution.Money a = new Solution.Money(1250, "USD");
        Solution.Money b = new Solution.Money(75, "USD");
        Solution.Money sum = a.plus(b);
        assertEquals(1325, sum.cents());
        assertEquals("USD", sum.currency());
        assertEquals(1250, a.cents());
        assertEquals(75, b.cents());
    }

    @Test
    @DisplayName("разные валюты складывать нельзя")
    void currencyMismatch() {
        assertThrows(IllegalArgumentException.class,
                () -> new Solution.Money(100, "USD").plus(new Solution.Money(100, "EUR")));
    }

    @Test
    @DisplayName("отрицательная сумма отвергается")
    void negative() {
        assertThrows(IllegalArgumentException.class, () -> new Solution.Money(-1, "USD"));
        assertEquals(0, new Solution.Money(0, "USD").cents());
    }

    @Test
    @DisplayName("равенство по сумме и валюте")
    void equality() {
        assertEquals(new Solution.Money(100, "USD"), new Solution.Money(100, "USD"));
        assertNotEquals(new Solution.Money(100, "USD"), new Solution.Money(100, "EUR"));
        assertNotEquals(new Solution.Money(100, "USD"), new Solution.Money(101, "USD"));
        assertNotEquals(new Solution.Money(100, "USD"), null);
        assertNotEquals(new Solution.Money(100, "USD"), "1.00 USD");
    }

    @Test
    @DisplayName("равные объекты имеют равный hashCode")
    void hash() {
        assertEquals(new Solution.Money(100, "USD").hashCode(), new Solution.Money(100, "USD").hashCode());
        Set<Solution.Money> set = new HashSet<>();
        set.add(new Solution.Money(500, "EUR"));
        assertTrue(set.contains(new Solution.Money(500, "EUR")));
        assertFalse(set.contains(new Solution.Money(500, "USD")));
    }

    @Test
    @DisplayName("toString с двумя цифрами копеек")
    void text() {
        assertEquals("12.50 USD", new Solution.Money(1250, "USD").toString());
        assertEquals("0.05 EUR", new Solution.Money(5, "EUR").toString());
        assertEquals("100.00 USD", new Solution.Money(10000, "USD").toString());
        assertEquals("0.00 USD", new Solution.Money(0, "USD").toString());
    }
}
