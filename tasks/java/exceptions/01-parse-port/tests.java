import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("обычные порты")
    void valid() {
        assertEquals(8080, Solution.parsePort("8080"));
        assertEquals(1, Solution.parsePort("1"));
        assertEquals(65535, Solution.parsePort("65535"));
    }

    @Test
    @DisplayName("пробелы по краям")
    void trimmed() {
        assertEquals(443, Solution.parsePort("  443 "));
    }

    @Test
    @DisplayName("не число")
    void notNumber() {
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort("80a"));
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort("8.5"));
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort(""));
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort("   "));
    }

    @Test
    @DisplayName("вне диапазона")
    void outOfRange() {
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort("0"));
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort("65536"));
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort("-1"));
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort("99999999999"));
    }

    @Test
    @DisplayName("null")
    void nullInput() {
        assertThrows(IllegalArgumentException.class, () -> Solution.parsePort(null));
    }
}
