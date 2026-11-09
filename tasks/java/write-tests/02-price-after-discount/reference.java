import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    @Test
    void percentDiscounts() {
        assertEquals(9000, Solution.priceAfterDiscount(10000, "SAVE10"));
        assertEquals(7500, Solution.priceAfterDiscount(10000, "SAVE25"));
    }

    @Test
    void discountIsFlooredToWholeCents() {
        assertEquals(1800, Solution.priceAfterDiscount(1999, "SAVE10"));
        assertEquals(1500, Solution.priceAfterDiscount(1999, "SAVE25"));
    }

    @Test
    void fixedDiscount() {
        assertEquals(1500, Solution.priceAfterDiscount(2000, "MINUS5"));
    }

    @Test
    void fixedDiscountDoesNotGoBelowZero() {
        assertEquals(0, Solution.priceAfterDiscount(300, "MINUS5"));
        assertEquals(0, Solution.priceAfterDiscount(500, "MINUS5"));
    }

    @Test
    void unknownCodeMeansNoDiscount() {
        assertEquals(1000, Solution.priceAfterDiscount(1000, "WELCOME"));
        assertEquals(1000, Solution.priceAfterDiscount(1000, ""));
        assertEquals(1000, Solution.priceAfterDiscount(1000, null));
    }

    @Test
    void codeIsCaseSensitive() {
        assertEquals(1000, Solution.priceAfterDiscount(1000, "save10"));
        assertEquals(1000, Solution.priceAfterDiscount(1000, "Minus5"));
    }

    @Test
    void zeroPrice() {
        assertEquals(0, Solution.priceAfterDiscount(0, "SAVE25"));
    }

    @Test
    void negativePrice() {
        assertThrows(IllegalArgumentException.class, () -> Solution.priceAfterDiscount(-1, "SAVE10"));
    }
}
