export async function summarize(tasks: Promise<unknown>[]): Promise<{ fulfilled: number; rejected: number }> {
  try {
    await Promise.all(tasks);
    return { fulfilled: tasks.length, rejected: 0 };
  } catch {
    return { fulfilled: 0, rejected: 1 };
  }
}
