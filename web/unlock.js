// Правило цепочки: задача открыта, если она первая в своём уровне (lang+topic+level)
// или решена предыдущая задача того же уровня. Чистая функция, без DOM.
export function taskState(task, allTasks, solved) {
  if (solved.has(task.id)) return "solved";
  const group = allTasks
    .filter(x => x.lang === task.lang && x.topic === task.topic && x.level === task.level)
    .sort((a, b) => a.order - b.order);
  const i = group.findIndex(x => x.id === task.id);
  if (i <= 0) return "open";
  return solved.has(group[i - 1].id) ? "open" : "locked";
}
