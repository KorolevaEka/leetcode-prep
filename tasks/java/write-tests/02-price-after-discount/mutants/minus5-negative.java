public class Solution {
    public static int priceAfterDiscount(int priceCents, String code) {
        if (priceCents < 0) {
            throw new IllegalArgumentException("price must not be negative");
        }
        if (code == null) {
            return priceCents;
        }
        int discount = 0;
        if (code.equals("SAVE10")) {
            discount = priceCents * 10 / 100;
        } else if (code.equals("SAVE25")) {
            discount = priceCents * 25 / 100;
        } else if (code.equals("MINUS5")) {
            discount = 500;
        }
        return priceCents - discount;
    }
}
