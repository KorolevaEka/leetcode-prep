export interface Selector {
  tag: string | null;
  id: string | null;
  classes: string[];
  attrs: Record<string, string>;
}

export function parseSelector(selector: string): Selector {
  throw new Error("TODO");
}
