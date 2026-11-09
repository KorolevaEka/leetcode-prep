export interface ParsedUrl {
  protocol: string;
  host: string;
  port: number | null;
  path: string;
  query: string;
  hash: string;
}


export function splitUrl(url: string): ParsedUrl {
  const protocolEnd = url.indexOf("://");
  const protocol = url.slice(0, protocolEnd);
  let rest = url.slice(protocolEnd + 3);

  let hash = "";
  let query = "";
  const queryAt = rest.indexOf("?");
  if (queryAt !== -1) {
    query = rest.slice(queryAt + 1);
    rest = rest.slice(0, queryAt);
  }
  const hashAt = rest.indexOf("#");
  if (hashAt !== -1) {
    hash = rest.slice(hashAt + 1);
    rest = rest.slice(0, hashAt);
  }

  const slashAt = rest.indexOf("/");
  const authority = slashAt === -1 ? rest : rest.slice(0, slashAt);
  const path = slashAt === -1 ? "/" : rest.slice(slashAt);

  const colonAt = authority.lastIndexOf(":");
  if (colonAt === -1) return { protocol, host: authority, port: null, path, query, hash };
  return { protocol, host: authority.slice(0, colonAt), port: Number(authority.slice(colonAt + 1)), path, query, hash };
}
