public class Solution {
    public static int priceAfterDiscount(int priceCents, String code) {
        if (priceCents < 0) {
            throw new IllegalArgumentException("price must not be negative");
        }
        int discount = 0;
        if (code.equals("SAVE10")) {
            discount = priceCents * 10 / 100;
        } else if (code.equals("SAVE25")) {
            discount = priceCents * 25 / 100;
        } else if (code.equals("MINUS5")) {
            discount = Math.min(500, priceCents);
        }
        return priceCents - discount;
    }
}
