export function compressRuns(lines: string[]): string[] {
  const out: string[] = [];
  let i = 0;
  while (i < lines.length - 1) {
    let j = i;
    while (j < lines.length && lines[j] === lines[i]) j++;
    const count = j - i;
    out.push(count > 1 ? `${lines[i]} (x${count})` : lines[i]);
    i = j;
  }
  return out;
}
