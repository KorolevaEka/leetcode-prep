package org.junit.jupiter.api;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;
import org.junit.jupiter.api.function.Executable;

// Подмножество JUnit 5 Assertions с теми же сообщениями об ошибках.
public final class Assertions {
    private Assertions() {}

    private static String fmt(Object v) { return "<" + (v instanceof Object[] a ? Arrays.deepToString(a) : String.valueOf(v)) + ">"; }
    private static String pre(String message) { return message == null || message.isEmpty() ? "" : message + " ==> "; }
    private static void check(boolean ok, Object expected, Object actual, String message) {
        if (!ok) throw new AssertionError(pre(message) + "expected: " + fmt(expected) + " but was: " + fmt(actual));
    }

    public static void assertEquals(Object expected, Object actual) { assertEquals(expected, actual, null); }
    public static void assertEquals(Object expected, Object actual, String message) { check(Objects.equals(expected, actual), expected, actual, message); }
    public static void assertEquals(int expected, int actual) { assertEquals((Object) expected, (Object) actual, null); }
    public static void assertEquals(int expected, int actual, String message) { assertEquals((Object) expected, (Object) actual, message); }
    public static void assertEquals(int expected, Integer actual) { assertEquals((Object) expected, actual, null); }
    public static void assertEquals(int expected, Integer actual, String message) { assertEquals((Object) expected, actual, message); }
    public static void assertEquals(Integer expected, int actual) { assertEquals(expected, (Object) actual, null); }
    public static void assertEquals(Integer expected, int actual, String message) { assertEquals(expected, (Object) actual, message); }
    public static void assertEquals(long expected, long actual) { assertEquals((Object) expected, (Object) actual, null); }
    public static void assertEquals(long expected, long actual, String message) { assertEquals((Object) expected, (Object) actual, message); }
    public static void assertEquals(long expected, Long actual) { assertEquals((Object) expected, actual, null); }
    public static void assertEquals(long expected, Long actual, String message) { assertEquals((Object) expected, actual, message); }
    public static void assertEquals(Long expected, long actual) { assertEquals(expected, (Object) actual, null); }
    public static void assertEquals(Long expected, long actual, String message) { assertEquals(expected, (Object) actual, message); }
    public static void assertEquals(char expected, char actual) { assertEquals((Object) expected, (Object) actual, null); }
    public static void assertEquals(char expected, char actual, String message) { assertEquals((Object) expected, (Object) actual, message); }
    public static void assertEquals(double expected, double actual) { assertEquals((Object) expected, (Object) actual, null); }
    public static void assertEquals(double expected, double actual, String message) { assertEquals((Object) expected, (Object) actual, message); }
    public static void assertEquals(double expected, double actual, double delta) { assertEquals(expected, actual, delta, null); }
    public static void assertEquals(double expected, double actual, double delta, String message) {
        check(Double.compare(expected, actual) == 0 || Math.abs(expected - actual) <= delta, expected, actual, message);
    }

    public static void assertNotEquals(Object unexpected, Object actual) { assertNotEquals(unexpected, actual, null); }
    public static void assertNotEquals(Object unexpected, Object actual, String message) {
        if (Objects.equals(unexpected, actual)) throw new AssertionError(pre(message) + "expected: not equal but was: " + fmt(actual));
    }

    public static void assertTrue(boolean condition) { assertTrue(condition, null); }
    public static void assertTrue(boolean condition, String message) { check(condition, true, false, message); }
    public static void assertFalse(boolean condition) { assertFalse(condition, null); }
    public static void assertFalse(boolean condition, String message) { check(!condition, false, true, message); }
    public static void assertNull(Object actual) { assertNull(actual, null); }
    public static void assertNull(Object actual, String message) { check(actual == null, null, actual, message); }
    public static void assertNotNull(Object actual) { assertNotNull(actual, null); }
    public static void assertNotNull(Object actual, String message) {
        if (actual == null) throw new AssertionError(pre(message) + "expected: not <null>");
    }

    public static void assertArrayEquals(int[] expected, int[] actual) { assertArrayEquals(box(expected), box(actual), null); }
    public static void assertArrayEquals(int[] expected, int[] actual, String message) { assertArrayEquals(box(expected), box(actual), message); }
    public static void assertArrayEquals(long[] expected, long[] actual) { assertArrayEquals(box(expected), box(actual), null); }
    public static void assertArrayEquals(long[] expected, long[] actual, String message) { assertArrayEquals(box(expected), box(actual), message); }
    public static void assertArrayEquals(Object[] expected, Object[] actual) { assertArrayEquals(expected, actual, null); }
    public static void assertArrayEquals(Object[] expected, Object[] actual, String message) {
        if (expected == actual) return;
        if (expected == null || actual == null) check(false, expected, actual, message);
        if (expected.length != actual.length) {
            throw new AssertionError(pre(message) + "array lengths differ, expected: <" + expected.length + "> but was: <" + actual.length + ">");
        }
        for (int i = 0; i < expected.length; i++) {
            if (!Objects.deepEquals(expected[i], actual[i])) {
                throw new AssertionError(pre(message) + "array contents differ at index [" + i + "], expected: " + fmt(expected[i]) + " but was: " + fmt(actual[i]));
            }
        }
    }
    public static void assertArrayEquals(char[] expected, char[] actual) { assertArrayEquals(box(expected), box(actual), null); }
    public static void assertArrayEquals(char[] expected, char[] actual, String message) { assertArrayEquals(box(expected), box(actual), message); }
    public static void assertArrayEquals(boolean[] expected, boolean[] actual) { assertArrayEquals(box(expected), box(actual), null); }
    public static void assertArrayEquals(boolean[] expected, boolean[] actual, String message) { assertArrayEquals(box(expected), box(actual), message); }
    public static void assertArrayEquals(double[] expected, double[] actual) { assertArrayEquals(expected, actual, 0.0, null); }
    public static void assertArrayEquals(double[] expected, double[] actual, String message) { assertArrayEquals(expected, actual, 0.0, message); }
    public static void assertArrayEquals(double[] expected, double[] actual, double delta) { assertArrayEquals(expected, actual, delta, null); }
    public static void assertArrayEquals(double[] expected, double[] actual, double delta, String message) {
        if (expected == actual) return;
        if (expected == null || actual == null) check(false, expected == null ? null : box(expected), actual == null ? null : box(actual), message);
        if (expected.length != actual.length) {
            throw new AssertionError(pre(message) + "array lengths differ, expected: <" + expected.length + "> but was: <" + actual.length + ">");
        }
        for (int i = 0; i < expected.length; i++) {
            if (Double.compare(expected[i], actual[i]) != 0 && !(Math.abs(expected[i] - actual[i]) <= delta)) {
                throw new AssertionError(pre(message) + "array contents differ at index [" + i + "], expected: " + fmt(expected[i]) + " but was: " + fmt(actual[i]));
            }
        }
    }
    private static Object[] box(char[] a) {
        if (a == null) return null;
        Object[] r = new Object[a.length];
        for (int i = 0; i < a.length; i++) r[i] = a[i];
        return r;
    }
    private static Object[] box(boolean[] a) {
        if (a == null) return null;
        Object[] r = new Object[a.length];
        for (int i = 0; i < a.length; i++) r[i] = a[i];
        return r;
    }
    private static Object[] box(double[] a) { return a == null ? null : Arrays.stream(a).boxed().toArray(); }
    private static Object[] box(int[] a) { return a == null ? null : Arrays.stream(a).boxed().toArray(); }
    private static Object[] box(long[] a) { return a == null ? null : Arrays.stream(a).boxed().toArray(); }

    public static void assertSame(Object expected, Object actual) { assertSame(expected, actual, null); }
    public static void assertSame(Object expected, Object actual, String message) {
        if (expected != actual) throw new AssertionError(pre(message) + "expected: same: " + fmt(expected) + " was not: " + fmt(actual));
    }
    public static void assertNotSame(Object unexpected, Object actual) { assertNotSame(unexpected, actual, null); }
    public static void assertNotSame(Object unexpected, Object actual, String message) {
        if (unexpected == actual) throw new AssertionError(pre(message) + "expected: not same but was: " + fmt(actual));
    }

    public static void assertIterableEquals(Iterable<?> expected, Iterable<?> actual) { assertIterableEquals(expected, actual, null); }
    public static void assertIterableEquals(Iterable<?> expected, Iterable<?> actual, String message) {
        if (expected == actual) return;
        if (expected == null || actual == null) check(false, expected, actual, message);
        Iterator<?> e = expected.iterator(), a = actual.iterator();
        int i = 0;
        while (e.hasNext() && a.hasNext()) {
            Object x = e.next(), y = a.next();
            if (!Objects.deepEquals(x, y)) {
                throw new AssertionError(pre(message) + "iterable contents differ at index [" + i + "], expected: " + fmt(x) + " but was: " + fmt(y));
            }
            i++;
        }
        if (e.hasNext() || a.hasNext()) {
            int en = i, an = i;
            while (e.hasNext()) { e.next(); en++; }
            while (a.hasNext()) { a.next(); an++; }
            throw new AssertionError(pre(message) + "Iterable lengths differ, expected: <" + en + "> but was: <" + an + ">");
        }
    }

    public static void assertAll(Executable... executables) { assertAll(null, executables); }
    public static void assertAll(String heading, Executable... executables) {
        List<Throwable> failures = new ArrayList<>();
        for (Executable ex : executables) {
            try { ex.execute(); } catch (Throwable t) { failures.add(t); }
        }
        if (failures.isEmpty()) return;
        StringBuilder sb = new StringBuilder(heading == null || heading.isEmpty() ? "Multiple Failures" : heading)
            .append(" (").append(failures.size()).append(failures.size() == 1 ? " failure)" : " failures)");
        for (Throwable t : failures) sb.append("\n\t").append(t instanceof AssertionError ? t.getMessage() : t.toString());
        throw new AssertionError(sb.toString());
    }

    public static <T extends Throwable> T assertThrows(Class<T> expectedType, Executable executable) { return assertThrows(expectedType, executable, null); }
    public static <T extends Throwable> T assertThrows(Class<T> expectedType, Executable executable, String message) {
        try {
            executable.execute();
        } catch (Throwable t) {
            if (expectedType.isInstance(t)) return expectedType.cast(t);
            AssertionError e = new AssertionError(pre(message) + "Unexpected exception type thrown, expected: <" + expectedType.getName() + "> but was: <" + t.getClass().getName() + ">");
            e.initCause(t);
            throw e;
        }
        throw new AssertionError(pre(message) + "Expected " + expectedType.getName() + " to be thrown, but nothing was thrown.");
    }

    public static void assertDoesNotThrow(Executable executable) { assertDoesNotThrow(executable, null); }
    public static void assertDoesNotThrow(Executable executable, String message) {
        try {
            executable.execute();
        } catch (Throwable t) {
            AssertionError e = new AssertionError(pre(message) + "Unexpected exception thrown: " + t);
            e.initCause(t);
            throw e;
        }
    }

    public static <V> V fail(String message) { throw new AssertionError(message); }
    public static <V> V fail() { throw new AssertionError(); }
}
