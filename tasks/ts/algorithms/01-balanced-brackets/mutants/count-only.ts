export function isBalanced(text: string): boolean {
  const open = { "(": 0, "[": 0, "{": 0 };
  const close = { ")": "(", "]": "[", "}": "{" } as const;
  for (const ch of text) {
    if (ch in open) open[ch as keyof typeof open]++;
    else if (ch in close) open[close[ch as keyof typeof close]]--;
  }
  return open["("] === 0 && open["["] === 0 && open["{"] === 0;
}
