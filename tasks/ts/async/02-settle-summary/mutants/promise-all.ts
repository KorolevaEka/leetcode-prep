export async function summarize(tasks: Promise<unknown>[]): Promise<{ fulfilled: number; rejected: number }> {
  await Promise.all(tasks);
  return { fulfilled: tasks.length, rejected: 0 };
}
