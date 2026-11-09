import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    @DisplayName("локатор по id")
    void byId() {
        assertEquals("#login", new Solution.ById("login").toCss());
    }

    @Test
    @DisplayName("локатор по классу")
    void byClass() {
        assertEquals(".btn-primary", new Solution.ByClass("btn-primary").toCss());
    }

    @Test
    @DisplayName("локатор по тегу")
    void byTag() {
        assertEquals("input", new Solution.ByTag("input").toCss());
    }

    @Test
    @DisplayName("локатор по атрибуту")
    void byAttribute() {
        assertEquals("[type=\"submit\"]", new Solution.ByAttribute("type", "submit").toCss());
    }

    @Test
    @DisplayName("цепочка локаторов через пробел")
    void chainOfThree() {
        List<Solution.Locator> path = List.of(
                new Solution.ByTag("form"), new Solution.ByClass("row"), new Solution.ByAttribute("type", "submit"));
        assertEquals("form .row [type=\"submit\"]", Solution.chain(path));
    }

    @Test
    @DisplayName("цепочка из одного элемента и пустая")
    void chainEdges() {
        assertEquals("#login", Solution.chain(List.of(new Solution.ById("login"))));
        assertEquals("", Solution.chain(List.of()));
    }
}
