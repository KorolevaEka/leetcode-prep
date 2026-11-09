export function countTags(tags: string[]): Record<string, number> {
  const counts = new Map<string, number>();
  for (const raw of tags) {
    const tag = raw.trim().toLowerCase();
    if (tag === "") continue;
    counts.set(tag, (counts.get(tag) ?? 0) + 1);
  }
  return Object.fromEntries(counts);
}
