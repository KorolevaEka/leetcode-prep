import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("чётный остаток делится поровну")
    void evenSplit() {
        assertEquals("check...test", Solution.shortenMiddle("checkout_with_promo_code_test", 12));
    }

    @Test
    @DisplayName("нечётный остаток: лишний символ в начале")
    void oddSplit() {
        assertEquals("ab...j", Solution.shortenMiddle("abcdefghij", 6));
        assertEquals("abc...ij", Solution.shortenMiddle("abcdefghij", 8));
    }

    @Test
    @DisplayName("короткая строка не меняется")
    void shortUntouched() {
        assertEquals("login_test", Solution.shortenMiddle("login_test", 10));
        assertEquals("", Solution.shortenMiddle("", 5));
    }

    @Test
    @DisplayName("длина ровно max не сокращается")
    void exactLength() {
        assertEquals("abcdef", Solution.shortenMiddle("abcdef", 6));
    }

    @Test
    @DisplayName("max = 3: остаётся только многоточие")
    void minimalMax() {
        assertEquals("...", Solution.shortenMiddle("abcdef", 3));
    }

    @Test
    @DisplayName("длина результата равна max")
    void resultLength() {
        assertEquals(15, Solution.shortenMiddle("a_very_long_scenario_name_for_checkout", 15).length());
    }

    @Test
    @DisplayName("max меньше 3: IllegalArgumentException")
    void tooSmallMax() {
        assertThrows(IllegalArgumentException.class, () -> Solution.shortenMiddle("abcdef", 2));
        assertThrows(IllegalArgumentException.class, () -> Solution.shortenMiddle("ab", 0));
    }
}
