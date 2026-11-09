export interface ParsedUrl {
  protocol: string;
  host: string;
  port: number | null;
  path: string;
  query: string;
  hash: string;
}

export function splitUrl(url: string): ParsedUrl {
  throw new Error("TODO");
}
