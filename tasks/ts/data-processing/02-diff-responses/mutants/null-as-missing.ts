export interface Diff {
  added: string[];
  removed: string[];
  changed: string[];
}


export function diffResponses(before: Record<string, unknown>, after: Record<string, unknown>): Diff {
  return {
    added: Object.keys(after).filter(key => before[key] == null).sort(),
    removed: Object.keys(before).filter(key => !Object.hasOwn(after, key)).sort(),
    changed: Object.keys(before)
      .filter(key => Object.hasOwn(after, key) && JSON.stringify(before[key]) !== JSON.stringify(after[key]))
      .sort(),
  };
}
