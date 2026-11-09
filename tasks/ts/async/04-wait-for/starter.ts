export interface WaitOptions {
  timeoutMs: number;
  intervalMs: number;
  now?: () => number;
  sleep?: (ms: number) => Promise<void>;
}

export async function waitFor(condition: () => boolean | Promise<boolean>, options: WaitOptions): Promise<void> {
  throw new Error("TODO");
}
