export interface Diff {
  added: string[];
  removed: string[];
  changed: string[];
}


export function diffResponses(before: Record<string, unknown>, after: Record<string, unknown>): Diff {
  return {
    added: Object.keys(after).filter(key => !Object.hasOwn(before, key)).sort(),
    removed: Object.keys(before).filter(key => !Object.hasOwn(after, key)).sort(),
    changed: Object.keys(before)
      .filter(key => Object.hasOwn(after, key) && before[key] !== after[key])
      .sort(),
  };
}
