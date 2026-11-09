export interface Selector {
  tag: string | null;
  id: string | null;
  classes: string[];
  attrs: Record<string, string>;
}


export function parseSelector(selector: string): Selector {
  const result: Selector = { tag: null, id: null, classes: [], attrs: {} };
  let i = 0;

  const readName = (): string => {
    const start = i;
    while (i < selector.length && !".#[".includes(selector[i])) i++;
    return selector.slice(start, i);
  };

  const tag = readName();
  if (tag !== "") result.tag = tag;

  while (i < selector.length) {
    const ch = selector[i++];
    if (ch === "#") {
      result.id = readName();
    } else if (ch === ".") {
      result.classes.push(readName());
    } else if (ch === "[") {
      let name = "";
      while (selector[i] !== "=" && selector[i] !== "]") name += selector[i++];
      let value = "";
      if (selector[i] === "=") {
        i++;
        const quote = selector[i] === '"' || selector[i] === "'" ? selector[i++] : "";
        const end = quote === "" ? "]" : quote;
        while (selector[i] !== end) value += selector[i++];
        if (quote !== "") i++;
      }
      i++;
      result.attrs[name] = value;
    }
  }
  return result;
}
