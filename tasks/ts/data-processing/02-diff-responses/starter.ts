export interface Diff {
  added: string[];
  removed: string[];
  changed: string[];
}

export function diffResponses(before: Record<string, unknown>, after: Record<string, unknown>): Diff {
  throw new Error("TODO");
}
