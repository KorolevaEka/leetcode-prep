export function compressRuns(lines: string[]): string[] {
  const out: string[] = [];
  let i = 0;
  while (i < lines.length) {
    let j = i;
    while (j < lines.length && lines[j] === lines[i]) j++;
    const count = lines.filter(l => l === lines[i]).length;
    out.push(count > 1 ? `${lines[i]} (x${count})` : lines[i]);
    i = j;
  }
  return out;
}
