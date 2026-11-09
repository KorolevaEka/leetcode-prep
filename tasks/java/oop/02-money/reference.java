import java.util.Objects;

public class Solution {
    public static final class Money {
        private final long cents;
        private final String currency;

        public Money(long cents, String currency) {
            if (cents < 0) {
                throw new IllegalArgumentException("cents must not be negative");
            }
            this.cents = cents;
            this.currency = currency;
        }

        public long cents() {
            return cents;
        }

        public String currency() {
            return currency;
        }

        public Money plus(Money other) {
            if (!currency.equals(other.currency)) {
                throw new IllegalArgumentException("currency mismatch");
            }
            return new Money(cents + other.cents, currency);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof Money)) {
                return false;
            }
            Money m = (Money) o;
            return cents == m.cents && currency.equals(m.currency);
        }

        @Override
        public int hashCode() {
            return Objects.hash(cents, currency);
        }

        @Override
        public String toString() {
            long rest = cents % 100;
            return cents / 100 + "." + (rest < 10 ? "0" : "") + rest + " " + currency;
        }
    }
}
