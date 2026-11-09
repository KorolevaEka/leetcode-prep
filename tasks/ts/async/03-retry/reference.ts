export async function retry<T>(
  action: () => Promise<T>,
  attempts: number,
  delayMs: number,
  sleep: (ms: number) => Promise<void> = ms => new Promise<void>(resolve => setTimeout(resolve, ms)),
): Promise<T> {
  let lastError: unknown;
  for (let attempt = 1; attempt <= attempts; attempt++) {
    try {
      return await action();
    } catch (error) {
      lastError = error;
      if (attempt < attempts) await sleep(delayMs);
    }
  }
  throw lastError;
}
