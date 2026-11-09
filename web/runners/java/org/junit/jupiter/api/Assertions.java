package org.junit.jupiter.api;

import java.util.Arrays;
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
    private static Object[] box(int[] a) { return a == null ? null : Arrays.stream(a).boxed().toArray(); }
    private static Object[] box(long[] a) { return a == null ? null : Arrays.stream(a).boxed().toArray(); }

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
