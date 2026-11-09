import { waitFor } from "./solution";

function fakeClock() {
  let time = 0;
  const sleeps: number[] = [];
  return {
    now: () => time,
    sleep: async (ms: number) => {
      sleeps.push(ms);
      time += ms;
    },
    sleeps,
  };
}

describe("waitFor", () => {
  test("условие истинно сразу — без паузы", async () => {
    const clock = fakeClock();
    let calls = 0;
    await waitFor(() => (++calls, true), { timeoutMs: 100, intervalMs: 50, ...clock });
    expect(calls).toBe(1);
    expect(clock.sleeps).toEqual([]);
  });

  test("условие становится истинным на третьей проверке", async () => {
    const clock = fakeClock();
    let calls = 0;
    await waitFor(() => ++calls === 3, { timeoutMs: 1000, intervalMs: 20, ...clock });
    expect(calls).toBe(3);
    expect(clock.sleeps).toEqual([20, 20]);
  });

  test("таймаут: проверка делается и после его истечения", async () => {
    const clock = fakeClock();
    let calls = 0;
    await expect(waitFor(() => (++calls, false), { timeoutMs: 100, intervalMs: 30, ...clock })).rejects.toThrow("Timeout");
    expect(calls).toBe(5);
  });

  test("граница таймаута: время вышло ровно на проверке", async () => {
    const clock = fakeClock();
    let calls = 0;
    await expect(waitFor(() => (++calls, false), { timeoutMs: 100, intervalMs: 50, ...clock })).rejects.toThrow("Timeout");
    expect(calls).toBe(3);
  });

  test("условие, ставшее истинным после таймаута, засчитывается", async () => {
    const clock = fakeClock();
    let calls = 0;
    await waitFor(() => ++calls === 3, { timeoutMs: 100, intervalMs: 60, ...clock });
    expect(calls).toBe(3);
  });

  test("асинхронное условие", async () => {
    const clock = fakeClock();
    let calls = 0;
    await waitFor(async () => ++calls === 2, { timeoutMs: 100, intervalMs: 10, ...clock });
    expect(calls).toBe(2);
  });

  test("ошибка из условия пробрасывается", async () => {
    const clock = fakeClock();
    let calls = 0;
    const broken = () => {
      calls++;
      throw new Error("selector is broken");
    };
    await expect(waitFor(broken, { timeoutMs: 100, intervalMs: 10, ...clock })).rejects.toThrow("selector is broken");
    expect(calls).toBe(1);
  });

  test("настоящие часы по умолчанию", async () => {
    let calls = 0;
    await waitFor(() => ++calls === 3, { timeoutMs: 500, intervalMs: 5 });
    expect(calls).toBe(3);
  });
});
