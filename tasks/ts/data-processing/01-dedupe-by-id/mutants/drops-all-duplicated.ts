export interface TestUser {
  id: number;
  name: string;
}


export function dedupeById(users: TestUser[]): TestUser[] {
  return users.filter(user => users.filter(other => other.id === user.id).length === 1);
}
