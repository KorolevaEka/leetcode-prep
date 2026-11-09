export interface TestUser {
  id: number;
  name: string;
}


export function dedupeById(users: TestUser[]): TestUser[] {
  const byId = new Map<number, TestUser>();
  for (const user of users) byId.set(user.id, user);
  return [...byId.values()];
}
