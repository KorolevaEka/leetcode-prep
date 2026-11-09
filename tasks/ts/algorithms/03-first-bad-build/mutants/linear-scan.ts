export function firstBad(isBad: (build: number) => boolean, total: number): number {
  for (let build = 1; build <= total; build++) {
    if (isBad(build)) return build;
  }
  return -1;
}
