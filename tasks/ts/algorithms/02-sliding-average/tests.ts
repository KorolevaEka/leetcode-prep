import { SlidingAverage } from "./solution";

describe("SlidingAverage", () => {
  test("пример из условия", () => {
    const avg = new SlidingAverage(3);
    expect([avg.add(10), avg.add(20), avg.add(30), avg.add(40)]).toEqual([10, 15, 20, 30]);
  });

  test("окно уже заполнено — старое вытесняется", () => {
    const avg = new SlidingAverage(2);
    avg.add(100);
    avg.add(0);
    expect(avg.add(50)).toBeCloseTo(25);
    expect(avg.add(50)).toBeCloseTo(50);
  });

  test("окно из одного значения", () => {
    const avg = new SlidingAverage(1);
    expect(avg.add(5)).toBe(5);
    expect(avg.add(9)).toBe(9);
  });

  test("пока окно не заполнено, делим на число значений", () => {
    const avg = new SlidingAverage(10);
    expect(avg.add(4)).toBe(4);
    expect(avg.add(8)).toBe(6);
  });

  test("отрицательные и дробные значения", () => {
    const avg = new SlidingAverage(2);
    avg.add(-1.5);
    expect(avg.add(0.5)).toBeCloseTo(-0.5);
  });
});
