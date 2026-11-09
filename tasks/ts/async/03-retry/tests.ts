import { retry } from "./solution";

function flaky(failures: number) {
  const state = { calls: 0 };
  const action = async () => {
    state.calls++;
    if (state.calls <= failures) throw new Error(`fail ${state.calls}`);
    return "ok";
  };
  return { state, action };
}

function recordSleep() {
  const delays: number[] = [];
  const sleep = async (ms: number) => {
    delays.push(ms);
  };
  return { delays, sleep };
}

describe("retry", () => {
  test("успех с первой попытки — без пауз", async () => {
    const { state, action } = flaky(0);
    const { delays, sleep } = recordSleep();
    expect(await retry(action, 3, 100, sleep)).toBe("ok");
    expect(state.calls).toBe(1);
    expect(delays).toEqual([]);
  });

  test("успех после двух неудач", async () => {
    const { state, action } = flaky(2);
    const { delays, sleep } = recordSleep();
    expect(await retry(action, 5, 100, sleep)).toBe("ok");
    expect(state.calls).toBe(3);
    expect(delays).toEqual([100, 100]);
  });

  test("все попытки неудачны — последняя ошибка", async () => {
    const { state, action } = flaky(10);
    const { delays, sleep } = recordSleep();
    await expect(retry(action, 3, 50, sleep)).rejects.toThrow("fail 3");
    expect(state.calls).toBe(3);
    expect(delays).toEqual([50, 50]);
  });

  test("одна попытка — без пауз", async () => {
    const { state, action } = flaky(1);
    const { delays, sleep } = recordSleep();
    await expect(retry(action, 1, 50, sleep)).rejects.toThrow("fail 1");
    expect(state.calls).toBe(1);
    expect(delays).toEqual([]);
  });

  test("настоящая пауза по умолчанию", async () => {
    const { action } = flaky(1);
    expect(await retry(action, 2, 5)).toBe("ok");
  });
});
