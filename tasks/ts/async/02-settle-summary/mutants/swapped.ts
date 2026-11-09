export async function summarize(tasks: Promise<unknown>[]): Promise<{ fulfilled: number; rejected: number }> {
  const results = await Promise.allSettled(tasks);
  return {
    fulfilled: results.filter(r => r.status === "rejected").length,
    rejected: results.filter(r => r.status === "fulfilled").length,
  };
}
