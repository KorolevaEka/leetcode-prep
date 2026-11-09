import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("простое название")
    void simple() {
        assertEquals("login_with_valid_password", Solution.toFileName("login with valid password"));
    }

    @Test
    @DisplayName("заглавные буквы")
    void upperCase() {
        assertEquals("cart_is_empty", Solution.toFileName("Cart is EMPTY"));
    }

    @Test
    @DisplayName("пробелы по краям")
    void edges() {
        assertEquals("logout", Solution.toFileName("  logout "));
    }

    @Test
    @DisplayName("несколько пробелов и таб между словами")
    void manySpaces() {
        assertEquals("open_profile_page", Solution.toFileName("open   profile\tpage"));
    }

    @Test
    @DisplayName("только пробелы")
    void blank() {
        assertEquals("", Solution.toFileName("   "));
    }
}
