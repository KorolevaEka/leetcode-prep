export interface WaitOptions {
  timeoutMs: number;
  intervalMs: number;
  now?: () => number;
  sleep?: (ms: number) => Promise<void>;
}

export async function waitFor(condition: () => boolean | Promise<boolean>, options: WaitOptions): Promise<void> {
  const { timeoutMs, intervalMs, now = Date.now, sleep = ms => new Promise<void>(resolve => setTimeout(resolve, ms)) } = options;
  const start = now();
  while (true) {
    try {
      if (await condition()) return;
    } catch {}
    if (now() - start >= timeoutMs) throw new Error(`Timeout after ${timeoutMs}ms`);
    await sleep(intervalMs);
  }
}
