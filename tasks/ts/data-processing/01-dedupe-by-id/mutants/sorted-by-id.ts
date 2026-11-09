export interface TestUser {
  id: number;
  name: string;
}


export function dedupeById(users: TestUser[]): TestUser[] {
  const seen = new Set<number>();
  return users.filter(user => {
    if (seen.has(user.id)) return false;
    seen.add(user.id);
    return true;
  }).sort((a, b) => a.id - b.id);
}
